from django.db import models

# Create your models here.
class Discount(models.Model):
    code = models.CharField(max_length=32)
    percentage = models.DecimalField(max_digits=50,decimal_places=4)
    expiry_date= models.DateTimeField()
    minimum_purchase_price=models.DecimalField(max_digits=50,decimal_places=4)

    def __str__(self):
        return self.code