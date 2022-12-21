from django.db import models
from users.models import User
from appservices.models import Service
from django.utils import timezone
from datetime import date
# Create your models here.

class PaymentUser1(models.Model):
    """Versión 1 del modelo de los pagos de los usuarios"""
    name_service=models.CharField(max_length=20)
    amount=models.FloatField()
    paymentDate=models.DateField(auto_now_add=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="client")
    def __str__(self):
        return f'{self.user}'

class PaymentUser2(models.Model):
    """Versión 2 del modelo de los pagos de los usuarios"""
        
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    service=models.ForeignKey(Service, on_delete=models.CASCADE, related_name="service")
    amount=models.FloatField()
    paymentDate=models.DateField(auto_now_add=True)
    expirationDate=models.DateField(default=date(2022,12,18))
    def __str__(self):
        return f'{self.user}'
       

class ExpiredPayments(models.Model):
    payment_user=models.ForeignKey(PaymentUser2, on_delete=models.CASCADE, related_name="payment_user")
    penalty_fee_amount=models.FloatField(default=25.0)
    
    
    