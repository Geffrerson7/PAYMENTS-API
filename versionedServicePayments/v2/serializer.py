from payments.models import PaymentUser2, ExpiredPayments
from appservices.models import Service
from rest_framework import serializers

class PaymentSerializerv2(serializers.ModelSerializer):
    """Serializer para la vista de los pagos"""
    service=serializers.SlugRelatedField(queryset=Service.objects.all(),slug_field="name")
    class Meta:
        model = PaymentUser2
        fields = 'email', 'service', 'amount','paymentDate','expirationDate','service_logo'
        read_only_fields = 'email','paymentDate','service_logo'

class PaymentExpiratedSerializerv2(serializers.ModelSerializer):
    """Serializer para la vista de los pagos expirados"""
    class Meta:
        model = ExpiredPayments
        fields = 'service_logo','service','paymentDate','amount','penalty_fee_amount','user'
        filter= 'user'
    
    
       
      
class ServiceSerializerv2(serializers.ModelSerializer):
    """Serializer para la vista de los servicios"""
    class Meta:
        model = Service
        fields = '__all__'
          