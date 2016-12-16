from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import generics
from .serializers import UsuarioSignUpSerializer, AddressSerializer, UsuariosSerializer
from .models import InfoUser

class UsuarioSignUp(generics.CreateAPIView):
	serializer_class = UsuarioSignUpSerializer

class Address(generics.CreateAPIView):
	serializer_class = AddressSerializer

class VendedoresView(generics.ListAPIView):
	queryset = InfoUser.objects.filter(groups__name="Vendedor")
	serializer_class = UsuariosSerializer