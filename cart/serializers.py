from rest_framework import serializers
from .models import CartItem
from products.serializers import ProductSerializer
from products.models import Product

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)  # full product data

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity']

class CartItemCreateSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta:
        model = CartItem
        fields = ['product', 'quantity']