from django.db import models

# Create your models here.

class UserRegistration(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile = models.CharField( max_length=15)
    password = models.CharField( max_length=50,  blank=True )

 
