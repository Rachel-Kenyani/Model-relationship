from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    birth_date= models.DateTimeField()
    email= models.EmailField()
    phone_number=  models.CharField(max_length=100)
    

    def __str__(self):
        return self.first_name