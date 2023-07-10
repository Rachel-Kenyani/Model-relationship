from django.db import models
from inventory.models import Product
# Create your models here.
class Shopping_cart(models.Model):
    user_id = models.CharField(max_length=32)
    product = models.ManyToManyField(Product, blank=False)
    total_price = models.DecimalField(max_digits=50,decimal_places=2)
    stock = models.PositiveIntegerField()
    
    def __str__(self):
        return self.user_id