from django.db import models
from vendors.models import Vendors

#Product model
class Products(models.Model):
    vendorName = models.ForeignKey(Vendors, on_delete = models.CASCADE)
    productName = models.CharField(max_length = 30)
    productDesc = models.TextField()
    productImage = models.ImageField()
    category = models.ManyToManyField(Category)
    slug = models.SlugField(max_length = 30, unique = True)

#category model
class Category(models.Model):
    categoryName = models.CharField(max_length = 100)
    slug = models.SlugField(max_length = 30, unique = True)

