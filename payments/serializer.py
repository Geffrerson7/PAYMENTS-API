from rest_framework import serializers
from .models import PaymentUser1, PaymentUser2, ExpiredPayments
from users.models import User
from appservices.models import Service
from datetime import datetime

class PaymentSerializer1(serializers.ModelSerializer):
    #user=serializers.SlugRelatedField(queryset=User.objects.all(),slug_field="username")
    class Meta:
        
        model = PaymentUser1
        fields = '__all__'
        read_only_fields = 'paymentDate','user',

class PaymentSerializerUser(serializers.ModelSerializer):
    #service=serializers.SlugRelatedField(queryset=Service.objects.all(),slug_field="name")
    
    class Meta:
        
        model = PaymentUser2
        fields = '__all__'
        read_only_fields = 'user','paymentDate','expirationDate',



class PaymentSerializerAdmin(serializers.ModelSerializer):
    user=serializers.SlugRelatedField(queryset=User.objects.all(),slug_field="email")
    service=serializers.SlugRelatedField(queryset=Service.objects.all(),slug_field="name")
    class Meta:
        
        model = PaymentUser2
        fields = '__all__'
        read_only_fields = 'user','paymentDate','expirationDate'

class PaymentExpiratedSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = ExpiredPayments
        fields = '__all__'
        read_only_fields = 'pay_user','penalty_fee_amount',