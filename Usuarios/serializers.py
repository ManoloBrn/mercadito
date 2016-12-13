from rest_framework import serializers
from mercadito import settings
from django.contrib.auth.models import User
from .models import InfoUser, Address

class UsuarioSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoUser
        fields = ["username", "email", "password", "businessName","groups"]

class AddressSerializer(serializers.ModelSerializer):
	class Meta:
		model = Address 
		fields = "__all__"