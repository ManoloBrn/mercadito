from django.db import models
from Inventarios.models import Producto
from mercadito import settings

# Create your models here.
class Bill(models.Model):
    estado = models.CharField(max_length=30, blank=True, default="Pago pendiente")
    payment_method = models.CharField(max_length=30, blank=False)
    date_added = models.DateTimeField(auto_now_add=True)

    #Relations
    cliente = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="client_bill")
    vendedor = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="store_bill")
    
    def __str__(self):
        return str(self.id)

class Item(models.Model):
    quantity = models.IntegerField(blank=False, default=0)
    subtotal = models.FloatField(blank=False, default=0.0)

    #Relations
    bill = models.ForeignKey(Bill, related_name="bill_items")
    product = models.ForeignKey(Producto, related_name="product_item")
    
    def __str__(self):
        return "Bill #" +str(self.bill.id)