from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from .forms import VendorSignupForm, VendorLoginForm
from django.http import HttpResponse

# Create your views here.
def test_view(request):
    return HttpResponse('Test View Successful!') 


def say_hello(request):
    return render(request, 'hello.html')

def vendor_home(request):
    return render(request, 'vendor_profile.html')

def vendor_signup(request):
    if request.method == 'POST':
        form = VendorSignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vendor account created successfully. Please log in.')
            return redirect('vendor_login')
    else:
        form = VendorSignupForm()
    return render(request, 'vendor_signup.html', {'form': form})

def vendor_login(request):
    if request.method == 'POST':
        form = VendorLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in successfully!')
                return redirect('vendor_dashboard')
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = VendorLoginForm()
    return render(request, 'vendor_login.html', {'form': form})
