import json
import random
import string
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.core.mail import send_mail
from .models import User, Customer, Vendor
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


class EmailUtils:
    @staticmethod
    def send_otp_service(email):
        otp = ''.join(random.choices(string.digits, k=6))
        subject = 'Your OTP for Password Reset'
        message = f'Your OTP is: {otp}'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [email]

        send_mail(subject, message, from_email,
                  recipient_list, fail_silently=False)

        return otp

    @staticmethod
    def send_new_password_service(email, new_password):
        subject = 'Your New Password'
        message = f'Your new password is: {new_password}'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [email]

        send_mail(subject, message, from_email,
                  recipient_list, fail_silently=False)


@method_decorator(csrf_exempt, name='dispatch')
class AddUserView(View):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body.decode('utf-8'))
            new_user = User.objects.create(
                username=data['username'],
                email=data['email'],
                password=data['password'],
                usertype=data['usertype']
            )
            return JsonResponse({'status': 'success', 'message': 'User added successfully'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'fullstack/home.html')


class ProfileView(View):
    def get(self, request, *args, **kwargs):
        email = request.session.get('email')
        username = request.session.get('username')
        usertype = request.session.get('usertype')
        # if you want to pass any information to the html file that render add additional parameters like email
        print(usertype)
        if (usertype == 'customer'):
            return render(request, 'fullstack/registration.html', {'email': email, 'username': username, 'usertype': usertype})
        else:
            return render(request, 'fullstack/vendor_reg.html', {'email': email, 'username': username, 'usertype': usertype})


@method_decorator(csrf_exempt, name='dispatch')
class CustomerView(View):
    def post(self, request, *args, **kwargs):
        print("hi")
        try:
            data = json.loads(request.body.decode('utf-8'))
            # Still need to save the customer data and need to retrive the more data in the login
            fullname = data.get('fullname')
            address = data.get('address')
            email = request.session.get('email')
            phone = data.get('phone')
            dob = data.get('dob')
            gender = data.get('gender')
            product_interested = data.get('productInterested')

            request.session['fullname'] = fullname
            request.session['address'] = address
            request.session['phone'] = phone
            request.session['dob'] = dob
            request.session['gender'] = gender
            request.session['product_interested'] = product_interested

            print("customer data")
            user = User.objects.get(username=email)
            customer = Customer.objects.create(
                user=user,
                fullname=fullname,
                address=address,
                phone=phone,
                dob=dob,
                gender=gender,
                product_interested=product_interested
            )

            return JsonResponse({'status': 'success', 'message': data, 'redirect_url': '/user/cdashboard/'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})


class CustomerDashBoardView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'fullstack/cdashboard.html', {
            'username': request.session.get('username'),
            'email': request.session.get('email'),
            'usertype': request.session.get('usertype'),
            'fullname': request.session.get('fullname'),
            'address': request.session.get('address'),
            'phone': request.session.get('phone'),
            'dob': request.session.get('dob'),
            'gender': request.session.get('gender'),
            'product_interested': request.session.get('product_interested')
        })
class LogoutView(View):
    def get(self, request, *args, **kwargs):
        print("hi")
        request.session.flush()
        return redirect('home')


@method_decorator(csrf_exempt, name='dispatch')
class VendorView(View):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body.decode('utf-8'))
            print("Vendor data", data)
            companyname = data.get('companyname')
            address = data.get('address')
            email = request.session.get('email')
            phone = data.get('phone')
            dob = data.get('dob')
            gender = data.get('gender')
            product_provided = data.get('productprovided')

            request.session['companyname'] = companyname
            request.session['address'] = address
            request.session['phone'] = phone
            request.session['dob'] = dob
            request.session['gender'] = gender
            request.session['product_provided'] = product_provided
            print("Vendor data")
            user = User.objects.get(username=email)
            vendor = Vendor.objects.create(
                user=user,
                companyname=companyname,
                address=address,
                phone=phone,
                dob=dob,
                gender=gender,
                product_provided=product_provided
            )
            return JsonResponse({'status': 'success', 'message': data, 'redirect_url': '/user/vboard/'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})


class VendorBoard(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'fullstack/vendorBoard.html', {
            'username': request.session.get('username'),
            'email': request.session.get('email'),
            'usertype': request.session.get('usertype'),
            'companyname': request.session.get('companyname'),
            'address': request.session.get('address'),
            'phone': request.session.get('phone'),
            'dob': request.session.get('dob'),
            'gender': request.session.get('gender'),
            'product_provided': request.session.get('product_provided')
        })
# shows after login


class MainPageView(View):
    def get(self, request, *args, **kwargs):
        email = request.session.get('email')
        username = request.session.get('username')
        usertype = request.session.get('usertype')
        # Render all the data stored in the session
        return render(request, 'fullstack/main.html', {'email': email, 'username': username, 'usertype': usertype})


@method_decorator(csrf_exempt, name='dispatch')
class SignupView(View):
    # def get(self, request, *args, **kwargs):
    #     # Handle GET request to render the signup form
    #     return render(request, 'fullstack/signup.html')
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body.decode('utf-8'))

            # Validate if passwords match
            password = data.get('password')
            confirm_password = data.get('confirm_password')

            if password != confirm_password:
                return JsonResponse({'status': 'error', 'message': 'Passwords do not match'})

            # Check if the user with the same email already exists
            if User.objects.filter(email=data['email']).exists():
                return JsonResponse({'status': 'error', 'message': 'User with the same email already exists'})
            # Create a new user
            new_user = User.objects.create(
                username=data['username'],
                email=data['email'],
                password=password,
                usertype=data['usertype']
            )
            request.session['username'] = data['username']
            request.session['email'] = data['email']
            request.session['usertype'] = data['usertype']

            # Check if the request wants JSON response
            return JsonResponse({'status': 'success', 'message': 'User signed up successfully', 'redirect_url': '/user/profile/'})

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})


@method_decorator(csrf_exempt, name='dispatch')
class LoginView(View):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body.decode('utf-8'))
            email = data.get('email')
            password = data.get('password')

            # Check if the user with the provided email and password exists
            user = User.objects.filter(email=email, password=password).first()
            print(user)

            if user:
                if user.usertype == 'customer':
                    common = Customer.objects.get(user=user)
                else:
                    common = Vendor.objects.get(user=user)
                print(common)
                print(user.usertype)
                # Add more details if you want
                request.session['username'] = user.username
                request.session['email'] = user.email
                request.session['usertype'] = user.usertype
                request.session['address'] = common.address
                request.session['phone'] = common.phone
                request.session['dob'] = common.dob.isoformat()
                request.session['gender'] = common.gender
                if (user.usertype == 'customer'):
                    request.session['fullname'] = common.fullname
                    request.session['product_interested'] = common.product_interested
                else:
                    request.session['companyname'] = common.companyname
                    request.session['product_provided'] = common.product_provided

                return JsonResponse({'status': 'success', 'redirect_url': '/user/cdashboard/'})
            else:
                return JsonResponse({'status': 'error', 'message': 'Email or password is incorrect'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message':str(e)})


# views.py

@method_decorator(csrf_exempt, name='dispatch')
class ForgetPasswordView(View):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body.decode('utf-8'))
            email = data.get('email')

            # Check if the user exists (you may need to customize this based on your User model)
            user = User.objects.get(email=email)

            # Send OTP to the user's email
            otp = EmailUtils.send_otp_service(email)

            # Store the OTP in the session for verification
            request.session['forget_password_otp'] = otp
            request.session['forget_password_user_email'] = email

            return JsonResponse({'status': 'success', 'message': 'OTP sent successfully'})
        except User.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'User does not exist'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})


@method_decorator(csrf_exempt, name='dispatch')
class VerifyOTPView(View):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body.decode('utf-8'))
            otp = data.get('otp')

            # Retrieve the stored OTP from the session
            stored_otp = request.session.get('forget_password_otp')
            user_email = request.session.get('forget_password_user_email')

            if stored_otp and user_email:
                if stored_otp == otp:
                    # Generate a new password
                    new_password = ''.join(random.choices(
                        string.ascii_letters + string.digits, k=6))

                    # Update the user's password
                    user = User.objects.get(email=user_email)
                    user.password = new_password
                    user.save()

                    # Send the new password to the user's email
                    EmailUtils.send_new_password_service(
                        user_email, new_password)

                    # Clear the session after successful verification
                    del request.session['forget_password_otp']
                    del request.session['forget_password_user_email']

                    return JsonResponse({'status': 'success', 'message': 'Password updated successfully'})
                else:
                    return JsonResponse({'status': 'error', 'message': 'Invalid OTP'})
            else:
                return JsonResponse({'status': 'error', 'message': 'OTP not found in session'})
        except User.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'User does not exist'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
