from django.db import models

# Create your models here.
class Vendor(models.Model):
    name = models.CharField(max_length=32)
    email= models.EmailField()
    phone_number=  models.CharField(max_length=100)
    

    def __str__(self):
        return self.name