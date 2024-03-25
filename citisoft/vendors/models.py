from django.db import models
from organiser.models import Products, Category

# Create your models here.
class Vendors(models.Model):
    vendorName = models.ForeignKey()
    businessName = models.CharField()
    vendorDesc = models.TextField()
    contactInfo = models.CharField()
    vendorImage = models.ImageField()
    slug =  models.SlugField(max_length = 30, unique = True)

    def __str__(self):
        return self.vendorName

class Customer(models.Model):
    userName = models.ForeignKey()
    emailAddress = models.CharField()
    slug = models.SlugField(max_length = 30, unique = True)

    def __str__(self):
        return self.userName

#represents a user wishlist
class Wishlist(models.Model):
    userName = models.ForeignKey(Customer, on_delete = models.CASCADE)
    wishlistName = models.CharField(max_length=255)
    dateCreated = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length = 30, unique = True)

#represent a product in the wishlist
class WishlistEntry(models.Model):
    userName = models.ForeignKey(Customer, on_delete = models.CASCADE)
    product = models.ForeignKey(Products, on_delete = models.CASCADE)
    wishlist = models.ForeignKey(Wishlist, on_delete = models.CASCADE, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add = True)
    slug = models.SlugField(max_length = 30, unique = True)