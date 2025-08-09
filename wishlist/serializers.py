from rest_framework import serializers
from .models import WishlistItem
from products.serializers import ProductSerializer
from products.models import Product

class WishlistItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = WishlistItem
        fields = ['id', 'product', 'created_at']


class WishlistAddSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = WishlistItem
        fields = ['product_id']

    def create(self, validated_data):
        user = self.context['request'].user
        product_id = validated_data['product_id']

        # Ensure product exists
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            raise serializers.ValidationError("Product not found.")

        wishlist_item, created = WishlistItem.objects.get_or_create(
            user=user,
            product=product
        )
        return wishlist_item
