from email.policy import default
from django.db import models

# Create your models here.



class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True, max_length=400)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)


