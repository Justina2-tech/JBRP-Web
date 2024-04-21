from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import VendorFormClass, CustomerForm, ProductForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import *


def indexA(request):
    return render(request,'dash/indexA.html')
def Home(request):
    return render(request,'dash/Home.html')
def vendorlist(request):
   vendors = VendorForm.objects.all()
   return render(request, 'dash/vendorlist.html',{'vendors':vendors})
def Product(request):
   products = ProductForm.objects.all()
   return render(request, 'dash/product.html',{'products':products})
def signup(request):
    return render (request, 'dash/signup.html')

def show_vendor_form(request):
    return render (request, 'dash/Vendorform.html')
def wishlist(request):
    return render(request, 'dash/wishlist.html')
def RemoveVform(request):
    return render(request,'dash/RemoveVform.html')
def profile(request):
    return render(request, 'dash/profile.html')

def product(request):
    products = ProductForm.objects.all()
    return render(request, 'dash/product.html',{'products':products})
def ProductForms(request):
    if request.method == 'POST':
        ProductName = request.POST['productName']
        description = request.POST['description']
        ProductForm.objects.create(Productname=ProductName,description=description)
        print('productName')

        #form = ProductForm(request.POST)  # Pass request data to the form
        #if form.is_valid():
        #form.save()  # Save the form if it's valid   
        return HttpResponse('Form submitted successfully!')
       
    else:
        
        return render(request, 'dash/ProductForm.html')
    
def VendorForms(request):
    if request.method == 'POST':
        vendorEmail = request.POST['contactEmail']
        vendorName = request.POST['vendorName']
        websiteUrl = request.POST['websiteUrl']
        description = request.POST['description']
        businessType = request.POST['businessType']
        address = request.POST['address']
        location = request.POST['location']
        postcode = request.POST['postcode']
        phoneNumber = request.POST['phoneNumber']
        totalProducts = request.POST['totalProducts']
        totalProducts = int(totalProducts)
        company_logo = request.FILES.get('company_logo')
        VendorForm.objects.create(vendor_name=vendorName,contact_email=vendorEmail,website_url=websiteUrl,description=description,business_type=businessType,address=address,location=location,postcode=postcode,phone_number=phoneNumber,total_products=totalProducts,company_logo=company_logo)
        print('contactEmail',vendorEmail)
    #    form = VendorFormClass(request.POST, request.FILES)  # Pass request data to the form
    #    if form.is_valid():
    #       form.save()  # Save the form if it's valid   
        return HttpResponse('Form submitted successfully!')
       
    else:
        return render(request, 'dash/VendorForm.html')


def customer_list(request):
    customers = Customer.objects.all()  # Accessing the Customer model's objects
    return render(request, 'dash/customer_list.html', {'customers': customers})

def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')  # Redirect to the customer list page
    else:
        form = CustomerForm()
    return render(request, 'add_customer.html', {'form': form})

def delete_vendor(request):
    if request.method == 'POST':
        vendorId = request.GET['vendorId']
        print('vendorId',vendorId)
        vendor = VendorForm.objects.get(pk=vendorId)
        vendor.delete()
        redirect('vendorlist')
        
    else:
        print('nothing')   
         
def delete_product(request):
    if request.method == 'POST':
        productId = request.GET['productId']
        print('productId',productId)
        product = ProductForm.objects.get(pk=productId)
        product.delete()
        redirect('product')
        
    else:
        print('nothing')    
       
def login(request):
    if request.method == 'POST':
        user_type = request.POST.get('user-type')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Authenticate user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Check if the user is active and staff
            if user.is_active and user.is_staff:
                # Log the user in                
                # Redirect users based on their user type
                if user_type == 'admin':
                     return render(request,'dash/indexA.html')
                elif user_type == 'vendor':
                    return redirect('vendor_dashboard')  # Replace 'vendor_dashboard' with your vendor dashboard URL name
                elif user_type == 'customer':
                    return redirect('customer_dashboard')  # Replace 'customer_dashboard' with your customer dashboard URL name
            else:
                # Inactive or non-staff user
                messages.error(request, 'Invalid credentials or access denied.')
        else:
            # Authentication failed
            messages.error(request, 'Invalid username or password.')
    
    # Render login page with form
    return render(request, 'dash/login.html')
