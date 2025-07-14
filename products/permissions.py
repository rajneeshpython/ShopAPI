from rest_framework import permissions

class IsVendorOrReadOnly(permissions.BasePermission):
    """
    - Allow safe methods (GET, HEAD) for all
    - Only vendors can write
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.is_vendor


class IsOwnerVendor(permissions.BasePermission):
    """
    - Only the product's vendor can update/delete it
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.vendor == request.user
