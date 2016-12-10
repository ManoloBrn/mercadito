from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Address(models.Model):
    addressOne = models.CharField(max_length=80, blank=False)
    colonia = models.CharField(max_length=20, blank=False)
    ciudad = models.CharField(max_length=15, blank=False)
    estado = models.CharField(max_length=20, blank=False)
    is_active = models.BooleanField(default=True)
    zipcode = models.CharField(max_length=5, blank=False)
    
    def __str__(self):
        return self.addressOne
    

class InfoUser(models.Model):
    user = models.ForeignKey(User, related_name="user_info")
    telephone = models.CharField(max_length=18)
    businessName = models.CharField(max_length=20, blank=True)
    images = models.FileField(upload_to="/uploads")
    address = models.ForeignKey(Address, related_name="user_address")
    
    def __string__(self):
        return self.user.email