from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import Category, Brand, Product
from .permissions import IsVendorOrReadOnly, IsOwnerVendor
from .serializers import CategorySerializer, BrandSerializer, ProductSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]  # only admin can create


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [permissions.IsAdminUser]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    filterset_fields = ['category', 'brand']
    search_fields = ['title', 'description']
    ordering_fields = ['price', 'created_at']
    permission_classes = [IsVendorOrReadOnly, IsOwnerVendor]

    def perform_create(self, serializer):
        serializer.save(vendor=self.request.user)
