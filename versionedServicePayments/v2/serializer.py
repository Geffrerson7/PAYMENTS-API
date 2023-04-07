from payments.models import PaymentUser2, ExpiredPayments, UserProfile
from appservices.models import Service
from rest_framework import serializers


class PaymentSerializerv2(serializers.ModelSerializer):
    service = serializers.SlugRelatedField(
        queryset=Service.objects.all(), slug_field="name"
    )

    class Meta:
        model = PaymentUser2
        fields = (
            "email",
            "service",
            "amount",
            "paymentDate",
            "expirationDate",
            "service_logo",
        )
        read_only_fields = "email", "paymentDate", "service_logo"


class PaymentExpiratedSerializerv2(serializers.ModelSerializer):
    class Meta:
        model = ExpiredPayments
        fields = (
            "service_logo",
            "service",
            "paymentDate",
            "amount",
            "penalty_fee_amount",
            "user",
        )


class ServiceSerializerv2(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = (
            "photo",
            "username",
            "id",
        )
        read_only_fields = ("username",)
