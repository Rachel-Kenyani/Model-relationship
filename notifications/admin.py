from django.contrib import admin

# Register your models here.
from .models import Notification

class NotificationAdmin(admin.ModelAdmin):
    list_display=('user_id','content','created_date')

admin.site.register(Notification,NotificationAdmin)