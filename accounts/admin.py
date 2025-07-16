from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


admin.site.site_header = "ShopZone Admin Panel"
admin.site.site_title = "ShopZone Admin Portal"
admin.site.index_title = "Welcome to ShopZone Dashboard"

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'email', 'username', 'is_vendor', 'is_customer', 'is_staff')
    list_filter = ('is_vendor', 'is_customer', 'is_staff', 'is_active')
    search_fields = ('email', 'username')
    ordering = ('id',)
    fieldsets = UserAdmin.fieldsets + (
        ('Roles', {'fields': ('is_vendor', 'is_customer')}),
    )
