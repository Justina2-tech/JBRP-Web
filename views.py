from django.shortcuts import render, redirect,HttpResponse,HttpResponseRedirect
from .forms import VendorForm


def indexA(request):
    return render(request,'dash/indexA.html')
def vendorlist(request):
    return render(request, 'dash/vendorlist.html')
def show_vendor_form(request):
    return render (request, 'dash/Vendorform.html')
def submit_VendorForm(request):
    if request.method == 'POST':
        form = VendorForm(request.POST, request.FILES)  # Pass request.FILES for file uploads
        if form.is_valid():
            form.save()

        # Save the form data to the database# Process the form data here
        
        return redirect("vendorlist2") 
    
    else:
        form = VendorForm()
            # If the request method is not POST, render the vendor form template
        return render(request, 'dash/vendorform.html', {'form': form})


def RemoveVform(request):
    return render(request, 'dash/RemoveVform.html')
def profile(request):
    return render(request, 'dash/profile.html')
def product(request):
    return render(request, 'dash/product.html')
def vendorlist2(request):
    return render(request, 'dash/vendorlist2.html')


