import json
import random
import string
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.core.mail import send_mail
from .models import User
from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

class EmailUtils:
    @staticmethod
    def send_otp_service(email):
        otp = ''.join(random.choices(string.digits, k=6))
        subject = 'Your OTP for Password Reset'
        message = f'Your OTP is: {otp}'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [email]

        send_mail(subject, message, from_email, recipient_list, fail_silently=False)

        return otp

    @staticmethod
    def send_new_password_service(email, new_password):
        subject = 'Your New Password'
        message = f'Your new password is: {new_password}'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [email]

        send_mail(subject, message, from_email, recipient_list, fail_silently=False)


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
        return render(request,'fullstack/home.html' )

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

            # Check if the request wants JSON response
            return JsonResponse({'status': 'success', 'message': 'User signed up successfully'})

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})

from django.http import JsonResponse

@method_decorator(csrf_exempt, name='dispatch')
class LoginView(View):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body.decode('utf-8'))
            email = data.get('email')
            password = data.get('password')

            # Check if the user with the provided email and password exists
            user = User.objects.filter(email=email, password=password).first()

            if user:
                return JsonResponse({'status': 'success', 'message': 'Login successful'})
            else:
                return JsonResponse({'status': 'error', 'message': 'Email or password is incorrect'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})



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
                    new_password = ''.join(random.choices(string.ascii_letters + string.digits, k=6))

                    # Update the user's password
                    user = User.objects.get(email=user_email)
                    user.password = new_password
                    user.save()

                    # Send the new password to the user's email
                    EmailUtils.send_new_password_service(user_email, new_password)

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
