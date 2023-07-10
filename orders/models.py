from django.db import models
from customer.models import Customer
# Create your models here.
class Order(models.Model):
    id = models.CharField(max_length=32)
    user = models.OneToOneField(Customer, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=50,decimal_places=4)
    address= models.CharField(max_length=32)
    order_date= models.DateTimeField(auto_now_add=True)
    delivery_date=models.DateTimeField()

    def __str__(self):
        return self.id

