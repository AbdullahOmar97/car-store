from rest_framework import permissions

class IsBuyerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow buyers of a car to edit or delete it.
    """

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.buyer == request.user
