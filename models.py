from django.db import models

# Create your models here.

CATAGORY_CHOICES={
    ('IW','IBM'),
    ('LI','Limina'),
    ('FD','Freyda'),
    ('EA','Ezops'),
    ('DY','Dynamo'),
    ('SP','Spark'),
    ('FB','Finbourne'),

}

class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    composition = models.TextField(default="")
    proapp = models.TextField(default="")
    category = models.CharField(choices=CATAGORY_CHOICES,max_length=2)
    product_image = models.ImageField(upload_to='product')
    def _str_(self):
        return self.title