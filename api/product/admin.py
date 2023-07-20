from django.contrib import admin
from django.contrib.admin import ModelAdmin

from . import models
from .models import Product
# Register your models here.


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'category', 'price', 'stock', 'is_active', 'image']
    search_display = ['name', 'description']
