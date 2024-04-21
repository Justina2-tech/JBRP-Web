from django import forms
from .models import VendorForm, Customer, ProductForm



class VendorFormClass(forms.ModelForm):
    class Meta:
        model = VendorForm
        fields = ['vendor_name', 'contact_email', 'website_url', 'business_type', 'address', 'location', 'postcode', 'phone_number', 'company_logo', 'total_products']
       
    def clean_vendor_name(self):
        vendor_name = self.cleaned_data.get('vendor_name')
        # Add your custom validation or processing here
        if len(vendor_name) < 3:
            raise forms.ValidationError("Vendor name must be at least 3 characters long.")
        return vendor_name

    def clean_contact_email(self):
        contact_email = self.cleaned_data.get('contact_email')
        # Add your custom validation or processing here
        if not contact_email.endswith('@example.com'):
            raise forms.ValidationError("Please use a valid email address ending with @example.com")
        return contact_email
    
    def clean_website_url(self):
        website_url = self.cleaned_data.get('website_url')
        # Add custom validation or processing here
        if not website_url.startswith('http://') and not website_url.startswith('https://'):
            website_url = 'http://' + website_url  # Prepend http:// if missing
        return website_url

    def clean_business_type(self):
        business_type = self.cleaned_data.get('business_type')
        # Add custom validation or processing here
        # For example, ensure it's one of the allowed choices
        allowed_choices = ['Retail', 'Service', 'Manufacturing', 'Consulting']
        if business_type not in allowed_choices:
            raise forms.ValidationError("Invalid business type.")
        return business_type

    def clean_address(self):
        address = self.cleaned_data.get('address')
        # Add custom validation or processing here
        return address

    def clean_location(self):
        location = self.cleaned_data.get('location')
        # Add custom validation or processing here
        return location

    def clean_postcode(self):
        postcode = self.cleaned_data.get('postcode')
        # Add custom validation or processing here
        return postcode




class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email']


class SignupForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    usertype = forms.ChoiceField(choices=[('Customer', 'Customer'), ('Vendor', 'Vendor')])
    

class ProductFormForm(forms.ModelForm):
    class Meta:
        model = ProductForm
        fields = ['Productname', 'description', 'image']
