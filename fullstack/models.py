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

