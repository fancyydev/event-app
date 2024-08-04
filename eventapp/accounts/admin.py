from django.contrib import admin
from .models import CustomUser
# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['email', 'name', 'phone', 'ticket', 'created']
    search_fields = ['email', 'name', 'phone']
    
admin.site.register(CustomUser, CustomUserAdmin)
