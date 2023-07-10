from django.contrib import admin

# Register your models here.
from .models import Payment

class PaymentAdmin(admin.ModelAdmin):
    list_display=('user_id','order_id','payment_method','total_price','transaction_id')

admin.site.register(Payment,PaymentAdmin)