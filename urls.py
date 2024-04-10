from django.urls import path 
from django.views.generic import RedirectView
from .import views

urlpatterns =[
  path('', views.indexA,name='dash'),
  path('indexA.html',views.indexA,name='dash'),
  path('vendorlist.html',views.vendorlist,name='vendorlist'),
  path('show_vendor_form.html',views.VendorForm,name='VendorForm'),
  path('profile.html',views.profile,name='profile'),
  path('RemoveVform.html',views.RemoveVform,name='RemoveVform'),
  path('submit_VendorForm/', views.submit_VendorForm, name='submit_VendorForm'),
  path('vendorlist2.html',views.vendorlist2,name='vendorlist2'),
]