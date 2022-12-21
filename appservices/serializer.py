from .models import Service
from rest_framework import serializers

class ServiceSerializer(serializers.ModelSerializer):
    """Serializer de la vista de los servicios"""
    class Meta:
        model = Service
        fields = '__all__'
          