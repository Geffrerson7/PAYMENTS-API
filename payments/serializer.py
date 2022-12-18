from rest_framework import serializers
from .models import Payment_user_1
from users.models import User

class PaymentSerializer1(serializers.ModelSerializer):
    #user=serializers.SlugRelatedField(queryset=User.objects.all(),slug_field="username")
    class Meta:
        model = Payment_user_1
        fields = '__all__'
        read_only_fields = 'paymentDate',