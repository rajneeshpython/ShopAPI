# cart/views.py

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import CartItem, Cart
from .serializers import CartItemSerializer, CartItemCreateSerializer

class CartItemViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def get_cart(self, user):
        return Cart.objects.get(user=user)

    def list(self, request):
        cart = self.get_cart(request.user)
        items = cart.items.select_related('product')
        serializer = CartItemSerializer(items, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = CartItemCreateSerializer(data=request.data)
        if serializer.is_valid():
            cart = self.get_cart(request.user)
            product = serializer.validated_data['product']
            quantity = serializer.validated_data['quantity']

            item, created = CartItem.objects.get_or_create(cart=cart, product=product)
            if not created:
                item.quantity += quantity
            else:
                item.quantity = quantity
            item.save()
            return Response(CartItemSerializer(item).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            cart = self.get_cart(request.user)
            item = CartItem.objects.get(pk=pk, cart=cart)
        except CartItem.DoesNotExist:
            return Response({"detail": "Item not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = CartItemCreateSerializer(item, data=request.data)
        if serializer.is_valid():
            item.quantity = serializer.validated_data['quantity']
            item.save()
            return Response(CartItemSerializer(item).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            cart = self.get_cart(request.user)
            item = CartItem.objects.get(pk=pk, cart=cart)
            item.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except CartItem.DoesNotExist:
            return Response({"detail": "Item not found."}, status=status.HTTP_404_NOT_FOUND)
