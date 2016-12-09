from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Address(models.Model):
    addressOne = models.CharField(max_length=80, blank=False)
    colonia = models.CharField(max_length=20, blank=False)
    ciudad = models.CharField(max_length=15, blank=False)
    estado = models.CharField(max_length=20, blank=False)
    is_active = models.BooleanField(default=True)
    

class InfoUser(models.Model):
    user = models.ForeignKey(User, related_name="user_info")
    telephone = models.CharField(max_length=18)
    businessName = models.CharField(max_length=20, blank=True)
    images = models.FileField(upload_to="/uploads")
    address = models.ForeignKey(Address, related_name="user_address")
    