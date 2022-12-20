from rest_framework import serializers
from .models import PaymentUser1, PaymentUser2, ExpiredPayments
from users.models import User
from appservices.models import Service
from datetime import datetime

class PaymentSerializer1(serializers.ModelSerializer):
    
    class Meta:
        
        model = PaymentUser1
        fields = 'name_service', 'amount','paymentDate','username',
        read_only_fields = 'paymentDate','username',

class PaymentSerializer(serializers.ModelSerializer):
    service=serializers.SlugRelatedField(queryset=Service.objects.all(),slug_field="name")
    class Meta:
        
        model = PaymentUser2
        fields = 'username', 'service', 'amount','paymentDate','expirationDate'
        read_only_fields = 'username','paymentDate','expirationDate'

class PaymentExpiratedSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = ExpiredPayments
        fields = 'user','penalty_fee_amount'
        read_only_fields = 'penalty_fee_amount','user'