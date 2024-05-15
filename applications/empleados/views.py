from django.shortcuts import render
from django.views.generic import  ListView
from rest_framework import viewsets
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView,
)
from rest_framework.pagination import PageNumberPagination
#!
from .serializers import EmpleadoSerializer , AdminSerializer
#?
from .models import Empleado


# Create your views here.

class CustomPagination(PageNumberPagination):
    page_size = 5  
    page_size_query_param = 'page_size' 
    max_page_size = 100  

class EmpleadosApiView(ListAPIView):
    serializer_class = EmpleadoSerializer
    pagination_class = CustomPagination
    
    def get_queryset(self):
        queryset = Empleado.objects.all()
        return queryset

class UpdateEmpleadosApiView(RetrieveUpdateAPIView):
    serializer_class = EmpleadoSerializer
    queryset = Empleado.objects.all()

class AdminView(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = AdminSerializer
