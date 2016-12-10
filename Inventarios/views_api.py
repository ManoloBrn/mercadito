from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import generics
from .models import Producto
from .serializers import ProductoSerializer

class ProductosList(viewsets.ViewSet):
    
     def list(self, request):
        queryset = Producto.objects.all()
        serializer = ProductoSerializer(queryset, many=True)
        return Response(serializer.data)
        
class ProductosCreate(generics.CreateAPIView):
    
    serializer_class = ProductoSerializer
    