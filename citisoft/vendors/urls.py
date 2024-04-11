from django.urls import path
from . import views

#URLConf
urlpatterns = [
    path('hello', views.say_hello),
    path('vendor_profile', views.vendor_home),
    path('login/', views.vendor_login, name='vendor_login'),
    path('signup/', views.vendor_signup, name='vendor_signup'),
    path('test/', views.test_view, name='test'),
]

