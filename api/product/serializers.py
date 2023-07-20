from rest_framework import serializers
from .models import Product
from ..category.serializers import CategorySerializer


class ProductSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, allow_empty_file=False, allow_null=True, required=False)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
