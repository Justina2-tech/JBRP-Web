from django.shortcuts import render, get_object_or_404, redirect
from .models import Vendor
from django.http import JsonResponse
from .forms import ProductForm
from organiser.models import Product, Category

def vendor_dashboard(request):
    #vendor = Vendor.objects.get(username=request.user.username)
    vendor = get_object_or_404(Vendor, username='addepar')
    total_products = Product.objects.filter(vendor=vendor).count() 
    products = Product.objects.filter(vendor=vendor)
    print(products)
    context = {'vendor': vendor,
               'current_page': 'home',
               'total_products': total_products,
               'products': products}
    return render(request, 'vendors/vendor_dashboard.html', context)

def manage_products(request, vendor_id):
    vendor = get_object_or_404(Vendor, username='addepar')  
    products = Product.objects.filter(vendor=vendor)
    context = {
        'vendor': vendor,
        'products': products,
    }
    return render(request, 'vendors/manage_products.html', context)


def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            vendor = get_object_or_404(Vendor, username='addepar')  # Fetch the vendor
            product.vendor = vendor  # Associate the vendor
            product.save()
            return redirect('manage-products', vendor_id=vendor.id)  # Redirect using the vendor's id 
    else:
        form = ProductForm()
    return render(request, 'vendors/create_product.html', {'form': form}) 

#def delete_product(request, product_id):
    if request.method == 'DELETE':
        product = get_object_or_404(Product, pk=product_id)
        if product.vendor == request.user.vendor:  # Ensure ownership
            product.delete()
            return JsonResponse({'success': True}) 
        else:
            return JsonResponse({'error': 'Unauthorized'}, status=401) 
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405) 
    

def delete_product(request, product_id):
    if request.method == 'DELETE':
        product = get_object_or_404(Product, pk=product_id)
        if product.vendor.username == 'addepar':  # Check against your vendor's username
            product.delete()
            return JsonResponse({'success': True}) 
        else:
            return JsonResponse({'error': 'Unauthorized'}, status=401) 
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405) 