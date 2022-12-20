from django.db import models
from users.models import User
from appservices.models import Service
from django.utils import timezone
from datetime import date
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
    paymentDate=models.DateField(auto_now_add=True)
    expirationDate=models.DateField(default=date(2022,12,18))
       
    def save(self, *args, **kwargs):
        if self.expirationDate > self.paymentDate:
            #payment=PaymentUser2.objects.get(id=)
            ExpiredPayments.objects.create(payment_user_id=self.pk)
       
        super().save(*args, **kwargs)
    
    def get_expirationDate(self):
        return self.expirationDate 
    
    def get_user(self):
        return self.user
    
    def get_amount(self):
        return self.amount

    def get_paymentDate(self):
        return self.expirationDate 
    

class ExpiredPayments(models.Model):
    payment_user=models.ForeignKey(PaymentUser2, on_delete=models.CASCADE, related_name="payment_user")
    penalty_fee_amount=models.FloatField(default=25.0)
    
    # def save(self, *args, **kwargs):
    #     payment=PaymentUser2.objects.get(expirationDate=timezone.now())
    #     self.penalty_fee_amount=0.1*payment.get_amount()
    #     self.pay_user=payment.get_user()
        
    #     super().save(*args, **kwargs)
    
    