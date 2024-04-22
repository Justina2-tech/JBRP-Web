from django.urls import path
from . import views

#URLConf
urlpatterns = [
    path('dashboard/', views.vendor_dashboard, name='vendor-dashboard'),
    path('products/<int:vendor_id>/', views.manage_products, name='manage-products'),
    path('products/create/', views.create_product, name='create-product'),
    path('products/delete/<int:product_id>/', views.delete_product, name='delete-product'), 
]