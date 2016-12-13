from django.db import models
from django.contrib.auth.models import User
from mercadito import settings
# Create your models here.
class Producto(models.Model):
    name = models.CharField(max_length=60, blank=False)
    description = models.CharField(max_length=100, blank=True)
    unitprice = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField(default=0)
    category = models.CharField(max_length=30, blank=False)
    images = models.FileField(upload_to="uploads/")
    vendedor = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="producto_vendedor")
    
    def __str__(self):
        return self.name