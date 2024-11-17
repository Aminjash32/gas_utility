from django.shortcuts import render
from rest_framework import viewsets
from .models import ServiceRequest
from .serializers import ServiceRequestSerializer

# Create your views here.
class ServiceRequestViewSet(viewsets.ModelViewSet):
    queryset = ServiceRequest.objects.all()
    serializer_class = ServiceRequestSerializer
