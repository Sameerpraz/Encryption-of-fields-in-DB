from django.db import models
from django_cryptography.fields import encrypt
# Create your models here.


class Customer(models.Model):
    name= models.CharField(max_length=500)
    address = encrypt(models.CharField(max_length=100))
    # address = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.address}'
        