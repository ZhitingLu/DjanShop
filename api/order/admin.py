from django.contrib import admin

from . import models
# Register your models here.


@admin.register(models.Order)
class CategoryAdmin(admin.ModelAdmin):
    """
    Sets how the model is shown in Django admin interface
    """
    list_display = ['id', 'user', ]
    search_fields = ['id', 'user', ]
