from django.urls import path
from .views import CartItemViewSet

cart_item_list = CartItemViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

cart_item_detail = CartItemViewSet.as_view({
    'put': 'update',
    'delete': 'destroy'
})

urlpatterns = [
    path('items/', cart_item_list, name='cartitem-list'),
    path('items/<int:pk>/', cart_item_detail, name='cartitem-detail'),
]
