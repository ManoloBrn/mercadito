from rest_framework import serializers
from .models import Bill, Item

class BillSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Bill
        fields= ["payment_method", "cliente", "vendedor"]
        
        
class ItemSerializer(serializers.ModelSerializer):
    bill_items = BillSerializer(many = False, read_only=False)
    class Meta:
        model = Item
        fields = ["quantity","product","bill_items"]
        

