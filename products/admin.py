from django.contrib import admin
from .models import Product, Category, Brand

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    ordering = ('id',)

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    ordering = ('id',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'vendor', 'price', 'stock', 'category', 'brand', 'is_active')
    list_filter = ('vendor', 'category', 'brand', 'is_active')
    search_fields = ('title', 'description', 'vendor__email')
    ordering = ('-created_at',)
