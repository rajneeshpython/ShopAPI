from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import WishlistItem
from .serializers import WishlistItemSerializer, WishlistAddSerializer


class WishlistItemViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return WishlistItem.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'create':
            return WishlistAddSerializer
        return WishlistItemSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

