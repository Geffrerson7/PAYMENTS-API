from rest_framework import serializers
from .models import PaymentUser1, PaymentUser2, ExpiredPayments
from appservices.models import Service


class PaymentSerializer1(serializers.ModelSerializer):
    class Meta:
        model = PaymentUser1
        fields = (
            "name_service",
            "amount",
            "paymentDate",
            "user",
        )
        read_only_fields = (
            "paymentDate",
            "user",
        )


class PaymentSerializer(serializers.ModelSerializer):
    service = serializers.SlugRelatedField(
        queryset=Service.objects.all(), slug_field="name"
    )

    class Meta:
        model = PaymentUser2
        fields = "email", "service", "amount", "paymentDate", "expirationDate"
        read_only_fields = "email", "paymentDate", "expirationDate"


class PaymentExpiratedSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpiredPayments
        fields = "amount", "penalty_fee_amount"
