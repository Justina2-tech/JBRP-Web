from django import forms
from organiser.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'product_desc', 'product_image', 'category']
