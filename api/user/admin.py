from django.contrib import admin

from . import models
# Register your models here.


@admin.register(models.CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'phone', 'gender', 'created_at', 'updated_at']
    search_display = ['id', 'name', 'email', 'gender']

