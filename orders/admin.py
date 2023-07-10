from django.contrib import admin

# Register your models here.
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display=('total_price', 'address', 'order_date', 'delivery_date','id')

admin.site.register(Order,OrderAdmin)