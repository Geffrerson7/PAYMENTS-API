from django.db import models
from users.models import User

# Create your models here.
class Payment_user_1(models.Model):
    """Versión 1 del modelo de las compras de usuarios"""
    name_service=models.CharField(max_length=20)
    amount=models.FloatField()
    paymentDate=models.DateField(auto_now_add=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="client")