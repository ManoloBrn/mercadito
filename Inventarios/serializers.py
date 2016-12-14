from rest_framework import serializers
from .models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = "__all__"

class ProductoVentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ["name", "description", "unitprice", "quantity"]