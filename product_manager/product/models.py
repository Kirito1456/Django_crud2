from django.db import models
from django.utils import timezone

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50)
    date_added = models.DateField(default= timezone.now())
    category = models.CharField(max_length=30, choices=[('Electronics', 'Electronics'), ('Clothing', 'Clothing'), ('Books', 'Books')])
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.name