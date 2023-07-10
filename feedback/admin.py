from django.contrib import admin

# Register your models here.
from .models import Review

class ReviewAdmin(admin.ModelAdmin):
    list_display=('author','product','rating','content','created_date','updated_date'
)

admin.site.register(Review,ReviewAdmin)