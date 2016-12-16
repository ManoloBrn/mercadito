from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework import status

class BillData(generics.CreateAPIView):
    serializer_class = ItemSerializer
    
    