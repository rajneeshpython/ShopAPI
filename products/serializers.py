from rest_framework import serializers
from .models import Category, Brand, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name', 'slug']


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    brand = BrandSerializer(read_only=True)
    vendor = serializers.StringRelatedField(read_only=True)  # shows email/username

    class Meta:
        model = Product
        fields = [
            'id', 'title', 'description', 'price',
            'stock', 'image', 'category', 'brand',
            'vendor', 'is_active', 'created_at'
        ]
