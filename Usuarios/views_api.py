from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import generics
from .serializers import UsuarioSignUpSerializer, AddressSerializer

class UsuarioSignUp(generics.CreateAPIView):
	serializer_class = UsuarioSignUpSerializer

class Address(generics.CreateAPIView):
	serializer_class = AddressSerializer