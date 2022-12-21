from payments.models import PaymentUser2, ExpiredPayments
from appservices.models import Service
from rest_framework import serializers

class PaymentSerializer(serializers.ModelSerializer):
    """Serializer para la vista de los pagos"""
    service=serializers.SlugRelatedField(queryset=Service.objects.all(),slug_field="name")
    class Meta:
        model = PaymentUser2
        fields = 'email', 'service', 'amount','paymentDate','expirationDate'
        read_only_fields = 'email','paymentDate','expirationDate'

class PaymentExpiratedSerializer(serializers.ModelSerializer):
    """Serializer para la vista de los pagos expirados"""
    class Meta:
        model = ExpiredPayments
        fields = 'user','penalty_fee_amount'
      
class ServiceSerializer(serializers.ModelSerializer):
    """Serializer para la vista de los servicios"""
    class Meta:
        model = Service
        fields = '__all__'
          