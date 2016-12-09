from django.db import models

# Create your models here.
class Productos(models.Model):
    name = models.CharField(max_length=60, blank=False)
    description = models.CharField(max_length=100, blank=True)
    unitprice = models.DecimalField()
    quantity = models.IntegerField()
    category = models.CharField(max_length=30, blank=False)
    images = models.FileField()
    vendedor = models.ForeignKey(Vendedor, related_name="producto-vendedor")