from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=30, unique=True)

    def __str__(self):
        return self.category_name
    
class Product(models.Model):
    vendor = models.ForeignKey('vendors.Vendor', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=30)
    product_desc = models.TextField()
    product_image = models.ImageField(upload_to='product_images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=30, unique=True)

    def __str__(self):
        return self.product_name
