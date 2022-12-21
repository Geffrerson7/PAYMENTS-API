from rest_framework import serializers
from .models import PaymentUser1, PaymentUser2, ExpiredPayments

class PaymentSerializer1(serializers.ModelSerializer):
    """Serializer para la vista de pagos de los usuarios (v1)"""
    class Meta:
        
        model = PaymentUser1
        fields = 'name_service', 'amount','paymentDate','user',
        read_only_fields = 'paymentDate','user',

class PaymentSerializer(serializers.ModelSerializer):
    """Serializer para la vista de pagos de los usuarios (v2)"""
    class Meta:
        
        model = PaymentUser2
        fields = 'user', 'service', 'amount','paymentDate','expirationDate'
        read_only_fields = 'user','paymentDate','expirationDate'

class PaymentExpiratedSerializer(serializers.ModelSerializer):
    """Serializer para la vista pagos expirados de los usuarios y admin"""
    class Meta:
        
        model = ExpiredPayments
        fields = 'payment_user','penalty_fee_amount'
        