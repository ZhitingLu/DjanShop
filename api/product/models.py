from django.db import models
from django.utils.html import format_html

from api.category.models import Category


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name="Product name")
    description = models.CharField(max_length=250, verbose_name="Product description")
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, verbose_name='Price')
    stock = models.PositiveIntegerField(null=False, blank=False, verbose_name='Stock')
    is_active = models.BooleanField(default=True, blank=True, verbose_name="Active")
    image = models.ImageField(upload_to="images/", blank=True, null=True, verbose_name="Product image")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name="product", blank=True, null=True,)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def show_picture(self):
        return format_html(
            '<img src="{}" class="icon-thumb" width="50" height="50" />',
            self.image.url)

    show_picture.short_description = 'Icon'

