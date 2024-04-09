from django import forms

class SignupForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    usertype = forms.ChoiceField(choices=[('Customer', 'Customer'), ('Vendor', 'Vendor')])
    
