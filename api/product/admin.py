from django.contrib import admin
from django.contrib.admin import ModelAdmin

from . import models
from .models import Product
# Register your models here.


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'category', 'price', 'stock', 'is_active', 'image']
    search_display = ['id', 'name', 'description']

    def show_picture(self, obj):
        return obj.show_picture()

    show_picture.short_description = 'Icon'
