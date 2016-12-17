from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from .models import *
from Inventarios.models import Producto
from Usuarios.models import InfoUser
from .serializers import *
from rest_framework import status

class BillData(generics.CreateAPIView):
    serializer_class = ItemSerializer

    def post(self,request, format=None):
    	quantity = request.data["quantity"]
    	productid = request.data["product"]
    	payment = request.data["bill_items.payment_method"]
    	clienteid = request.data["bill_items.cliente"]
    	vendedorid = request.data["bill_items.vendedor"]
    	cliente = InfoUser.objects.filter(id=int(clienteid))[0]
    	vendedor = InfoUser.objects.filter(id=int(vendedorid))[0]
    	bill = Bill(payment_method=payment,
    				cliente = cliente,
    				vendedor = vendedor)
    
    	bill.save()
    	product = Producto.objects.filter(id=int(productid))[0]
    	subtotal = product.unitprice*int(quantity)
    	billid = bill.id
    	item = Item(quantity = int(quantity),
    		subtotal=subtotal,
    		bill=bill,
    		product=product)

    	item.save()
    	return Response("Producto Creado")

    	#return Response("Error")
class BillList(generics.ListAPIView):
	queryset=Item.objects.all()
	serializer_class = ItemSerializer
    
class BillIdList(APIView):
    
    def get(self,request, pk, format=None):
        items = Item.objects.filter(bill__id=pk)
        serializer = ItemSerializer(items, many=True)
        
        return Response(serializer.data)
