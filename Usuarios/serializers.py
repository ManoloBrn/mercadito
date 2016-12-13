from rest_framework import serializers
from mercadito import settings
from django.contrib.auth.models import User
from .models import InfoUser, Address

class UsuarioCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoUser
        fields = ["username", "password", "businessName",
        		"first_name", "last_name"]

class AddressSerializer(serializers.ModelSerializer):
	class Meta:
		model = Address 
		fields = "__all__"