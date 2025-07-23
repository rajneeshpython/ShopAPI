from rest_framework import serializers
from .models import Order, OrderItem
from cart.models import Cart
from products.serializers import ProductSerializer

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = ['product', 'quantity', 'price']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'status', 'created_at', 'total_price', 'items']
        read_only_fields = ['id', 'created_at', 'total_price', 'items']

class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = []  # We don't need input; cart → order is automatic

    def create(self, validated_data):
        user = self.context['request'].user
        cart = Cart.objects.get(user=user)
        cart_items = cart.items.select_related('product')

        if not cart_items.exists():
            raise serializers.ValidationError("Cart is empty.")

        total_price = sum(item.product.price * item.quantity for item in cart_items)

        order = Order.objects.create(customer=user, total_price=total_price)

        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price  # snapshot
            )

        cart.items.all().delete()  # clear cart after order
        return order
