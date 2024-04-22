from django.db import models
from django_extensions.db.fields import AutoSlugField 

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='category_name', unique=True)


    def __str__(self):
        return self.category_name
    
class Product(models.Model):
    vendor = models.ForeignKey('vendors.Vendor', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=30)
    product_desc = models.TextField()
    product_image = models.ImageField(upload_to='product_images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = AutoSlugField(populate_from='product_name', unique=True)

    def __str__(self):
        return self.product_name
