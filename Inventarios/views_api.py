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
    
class ProductoUsuario(generics.ListAPIView):
    queryset = Producto.objects
    def get(self,request, pk, format=None):
        self.queryset = self.queryset.filter(vendedor=int(pk))
        serializer = ProductoSerializer(self.get_queryset(), many=True)
        
        return Response(serializer.data)