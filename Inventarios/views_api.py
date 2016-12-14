from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import generics
from .models import Producto
from .serializers import ProductoSerializer
from rest_framework import status

class ProductosList(viewsets.ViewSet):
     def list(self, request):
        queryset = Producto.objects.all()
        serializer = ProductoSerializer(queryset, many=True)
        return Response(serializer.data)
        
class ProductosCreate(generics.CreateAPIView):
    serializer_class = ProductoSerializer
    def post(self,request, format=None):
        serializer  = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"Ok"}, status = status.HTTP_201_CREATED)
        return Response({"status":"error"}, status = status.HTTP_400_BAD_REQUEST)
   
    
class ProductoUsuario(generics.ListAPIView):
    queryset = Producto.objects
    def get(self,request, pk, format=None):
        self.queryset = self.queryset.filter(vendedor=int(pk)).filter(vendedor__groups__name="Vendedor")
        serializer = ProductoSerializer(self.get_queryset(), many=True)
        
        return Response(serializer.data)