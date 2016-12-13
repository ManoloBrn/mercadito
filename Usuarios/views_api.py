from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import generics
from .serializers import UsuarioCreateSerializer, AddressSerializer

class UsuariosCreate(generics.CreateAPIView):
	serializer_class = UsuarioCreateSerializer

class Address(generics.CreateAPIView):
	serializer_class = AddressSerializer