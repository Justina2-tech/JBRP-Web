from django.urls import path
from ..views import SignupView, LoginView, ForgetPasswordView, VerifyOTPView,ProfileView,MainPageView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'), 
    path('login/', LoginView.as_view(), name='login'),
    path('profile/',ProfileView.as_view(), name='profile'),
    path('main/',MainPageView.as_view(), name='main'),
    path('forget-password/', ForgetPasswordView.as_view(), name='forget_password'),
    path('verify-otp/', VerifyOTPView.as_view(), name='verify_otp'),
    

]
