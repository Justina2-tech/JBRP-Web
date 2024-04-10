# forms.py

from django import forms
from .models import VendorForm

class VendorForm(forms.ModelForm):
    class Meta:
        model = VendorForm
        fields = ['vendor_name', 'contact_email', 'website_url', 'business_type', 'address', 'location', 'postcode', 'phone_number', 'company_logo', 'total_products']
       
    widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        } 