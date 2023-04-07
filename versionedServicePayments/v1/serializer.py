from rest_framework import serializers
from payments.models import PaymentUser1


class PaymentSerializerv1(serializers.ModelSerializer):
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
