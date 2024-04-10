from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.

class VendorForm(models.Model):  # Corrected class name
    vendor_name = models.CharField(max_length=100)
    contact_email = models.EmailField()
    website_url = models.URLField(blank=True)
    Description = models.TextField(default='')
    business_type = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    postcode = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    company_logo = models.ImageField(upload_to='logos/', blank=True)
    total_products = models.PositiveIntegerField()

    def __str__(self):
        return self.vendor_name
    
    class Meta:  # Corrected class name
        db_table = 'VendorForm'
        
    
    
