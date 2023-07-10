from django.contrib import admin

# Register your models here.
from .models import Discount

class DiscountAdmin(admin.ModelAdmin):
    list_display=('code','percentage','expiry_date','minimum_purchase_price'
)

admin.site.register(Discount,DiscountAdmin)