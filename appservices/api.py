from .models import Service
from .serializer import ServiceSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import viewsets
from .pagination import StandardResultsSetPagination


class ServiceUserViewSet(viewsets.ModelViewSet):
    """Vista de los servicios para los usuarios"""
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes=[IsAuthenticated]
    http_method_names=['get']
    throttle_scope = 'services-user'

class ServiceAdminViewSet(viewsets.ModelViewSet):
    """Vista de los servicios para el admin"""
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes=[IsAdminUser]
    
    
    
    