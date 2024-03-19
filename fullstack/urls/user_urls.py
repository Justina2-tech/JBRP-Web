from django.urls import path
from ..views import SignupView, LoginView, ForgetPasswordView, VerifyOTPView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'), 
    path('login/', LoginView.as_view(), name='login'),
    path('forget-password/', ForgetPasswordView.as_view(), name='forget_password'),
    path('verify-otp/', VerifyOTPView.as_view(), name='verify_otp'),
    

]
