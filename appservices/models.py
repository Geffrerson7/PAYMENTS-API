from django.db import models

# Create your models here.
class Service(models.Model):
    """Modelo de los servicios"""
    name=models.CharField(max_length=200)
    prefixe=models.CharField(max_length=200, default="")
    logo=models.URLField()
    
    def __str__(self):
         return self.name