from django.db import models
from users.models import User
from appservices.models import Service
from PIL import Image
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
    @property
    def email(self):
        return self.user.email
    @property
    def service_logo(self):
        return self.service.logo

    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    service=models.ForeignKey(Service, on_delete=models.CASCADE, related_name="service")
    amount=models.FloatField()
    paymentDate=models.DateField(auto_now_add=True)
    expirationDate=models.DateField()
    def __str__(self):
        return f'{self.user}'
       

class ExpiredPayments(models.Model):
    @property
    def user(self):
        return self.payment_user.user.email
    @property
    def service_logo(self):
        return self.payment_user.service.logo
    @property
    def service(self):
        return self.payment_user.service.name
    @property
    def amount(self):
        return self.payment_user.amount
    @property
    def paymentDate(self):
        return self.payment_user.paymentDate
    payment_user=models.ForeignKey(PaymentUser2, on_delete=models.CASCADE, related_name="payment_user")
    penalty_fee_amount=models.FloatField(default=0.0)
    
from PIL import Image


class Avatar(models.Model):
    name=models.CharField(max_length=200, default="")
    image = models.ImageField(default="default-profile.jpg", upload_to="profile_image")

    # def save(self, *args, **kwargs):
    #     super(Profile,self).save(*args, **kwargs)
    #     if self.image:
    #         img = Image.open(self.image.path)
    #         if img.height > 300 or img.width > 300:
    #             output_size = (300, 300)
    #             img.thumbnail(output_size)
    #             img.save(self.image.path)
