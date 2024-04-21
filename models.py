from django.db import models
from django.core.exceptions import ValidationError
import os
from pathlib import Path
from django.core.files.storage import FileSystemStorage
BASE_DIR = Path(__file__).resolve().parent.parent
MEDIA_ROOT = os.path.join(BASE_DIR,'static/images' )
fs = FileSystemStorage(location=MEDIA_ROOT)




# Create your models here.

class VendorForm(models.Model):  # Corrected class name
    vendor_name = models.CharField(max_length=100)
    contact_email = models.EmailField()
    website_url = models.URLField(blank=True)
    description = models.TextField(default='')
    business_type = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    postcode = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    company_logo = models.ImageField(upload_to='',storage=fs, blank=True,null=True)
    total_products = models.PositiveIntegerField()

    def __str__(self):
        return self.vendor_name
    
    @property
    def companyLogo(self):
        try:
            url = self.company_logo.url
        except:
            url = ''
        
        return url
    
    class Meta:  # Corrected class name
        db_table = 'VendorForm'
        
    

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.name    
    class meta:
        db_table = 'Customer'



class User(models.Model):
    userid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    usertype = models.CharField(max_length=50)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'user'  # Specify the custom table name
        

class ProductForm(models.Model):
    Productname = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    # Add any other fields you need for your products
    
    def __str__(self):
        return self.Productname
    
    class Meta:
        db_table = 'ProductForm'


