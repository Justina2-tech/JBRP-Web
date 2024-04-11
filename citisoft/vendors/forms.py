from django import forms
from django.contrib.auth.models import User  # For user authentication
from .models import Vendor

class VendorSignupForm(forms.ModelForm):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = Vendor
        fields = ['username', 'email', 'vendor_name', 'business_name', 'vendor_desc', 'phone_number', 'website']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords don\'t match')
        return password2

    def save(self, commit=True):
        user = User.objects.create_user(self.cleaned_data['username'], self.cleaned_data['email'], self.cleaned_data['password1'])
        vendor = self.instance
        vendor.user = user
        if commit:
            vendor.save()
        return vendor
    
class VendorLoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)