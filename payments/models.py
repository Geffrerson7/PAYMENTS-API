from django.db import models
from users.models import User
from appservices.models import Service
from django.utils import timezone
from datetime import timedelta, datetime
# Create your models here.

class PaymentUser1(models.Model):
    """Versión 1 del modelo de las compras de usuarios"""
    name_service=models.CharField(max_length=20)
    amount=models.FloatField()
    paymentDate=models.DateField(auto_now_add=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="client")

class PaymentUser2(models.Model):
    """Versión 2 del modelo de las compras de usuarios"""
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    service=models.ForeignKey(Service, on_delete=models.CASCADE, related_name="service")
    amount=models.FloatField()
    paymentDate=models.DateTimeField(auto_now_add=True)
    expirationDate=models.DateTimeField()
       
    def save(self, *args, **kwargs):
        self.expirationDate=timezone.now()+timedelta(minutes=1)
        super().save(*args, **kwargs)
    
    def get_expirationDate(self):
        return self.expirationDate 
    
    def get_user(self):
        return self.user
    
    def get_amount(self):
        return self.amount
    

class ExpiredPayments(models.Model):
    pay_user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="pay_user")
    penalty_fee_amount=models.FloatField()
    
    def save(self, *args, **kwargs):
        payment=PaymentUser2.objects.get(expirationDate=datetime.utcnow())
        self.penalty_fee_amount=0.1*payment.get_amount()
        self.pay_user=payment.get_user()
        
        super().save(*args, **kwargs)