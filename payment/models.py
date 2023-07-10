from django.db import models

# Create your models here.
class Payment(models.Model):
    user_id = models.CharField(max_length=32)
    order_id = models.CharField(max_length=32)
    payment_method = models.CharField(max_length=32)
    total_price = models.DecimalField(max_digits=50,decimal_places=4)
    transaction_id= models.CharField(max_length=32)
    

    def __str__(self):
        return self.user_id