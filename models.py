from django.db import models


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


class Customer(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='customer_profile')
    fullname = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    product_interested = models.CharField(max_length=100)


class Vendor(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='vendor_profile')
    companyname = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    product_provided = models.CharField(max_length=100)
