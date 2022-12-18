from .models import Service
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ServiceSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework import viewsets
from .pagination import StandardResultsSetPagination

#LISTA DE SERVICIOS PARA EL USUARIO
class GetAllService(APIView):
    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsSetPagination
    throttle_scope = 'services'

    def get(self, request):
        services = Service.objects.all()
        serializer = ServiceSerializer(services, many = True)
        return Response(serializer.data)
  
#CRUD ADMIN
class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes=[IsAdminUser]
    
    
    