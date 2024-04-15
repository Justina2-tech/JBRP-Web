from django.db import models
from django.contrib.auth.models import User

class Vendoralt(models.Model):
    vendor_name = models.CharField(max_length=100)
    business_name = models.CharField(max_length=100)
    vendor_desc = models.TextField()
    contact = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    website = models.URLField(blank=True, null=True) 
    vendor_image = models.ImageField(upload_to='vendor_images/')
    slug = models.SlugField(max_length=30, unique=True)

    def __str__(self):                             
        return self.business_name

class Vendor(models.Model):
    username = models.CharField(max_length=100, default='unknown')
    vendor_name = models.CharField(max_length=100)
    business_name = models.CharField(max_length=100)
    vendor_desc = models.TextField()
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    website = models.URLField(blank=True, null=True) 
    vendor_image = models.ImageField(upload_to='vendor_images/')
    slug = models.SlugField(max_length=30, unique=True)
 
    def __str__(self):                             
        return self.business_name 

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    slug = models.SlugField(max_length=30, unique=True)

    def __str__(self):
        return self.user.username    

class Wishlist(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    wishlist_name = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=30, unique=True)

    def __str__(self):
        return self.wishlist_name

class WishlistEntry(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey('organiser.Product', on_delete=models.CASCADE)
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=30, unique=True)
