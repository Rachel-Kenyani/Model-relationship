from django.contrib import admin

# Register your models here.
from .models import Shopping_cart

class Shopping_cartAdmin(admin.ModelAdmin):
    list_display=("user_id","total_price","stock")

admin.site.register(Shopping_cart,Shopping_cartAdmin)