from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=200)
    prefixe = models.CharField(max_length=200, default="")
    logo = models.URLField()

    def __str__(self):
        return self.name
