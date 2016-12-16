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
    

class InfoUser(AbstractUser):
   
    telephone = models.CharField(max_length=18, blank=True)
    businessName = models.CharField(max_length=20, blank=True)
    images = models.FileField(upload_to="/uploads", blank=True)
    address = models.ForeignKey(Address, related_name="user_address", default=1)
    
    def __string__(self):
        return self.user.email