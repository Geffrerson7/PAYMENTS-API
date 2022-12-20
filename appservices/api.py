from .models import Service
from .serializer import ServiceSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import viewsets
from .pagination import StandardResultsSetPagination

#VISTA DE SERVICIOS PARA EL USUARIO
class ServiceUserViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes=[IsAuthenticated]
    http_method_names=['get']
    throttle_scope = 'services-user'

#CRUD SERVICIOS ADMIN
class ServiceAdminViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes=[IsAdminUser]
    
    
    
    