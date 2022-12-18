from .models import Service
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ServiceSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication

class GetAllService(APIView):
    authentication_classes=[BasicAuthentication]
    permission_classes = [IsAuthenticated]
    throttle_scope = 'services'

    def get(self, request):
        services = Service.objects.all()
        serializer = ServiceSerializer(services, many = True)
        return Response(serializer.data)