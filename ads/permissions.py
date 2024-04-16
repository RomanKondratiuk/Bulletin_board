from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    message = 'You are not a owner!'

    def has_object_permission(self, request, view, obj):
        if request.user == obj.author:
            return True
        return False


class IsAdmin(BasePermission):
    """
    Allows access only to admin users.
    """
    def has_permission(self, request, view):
        return request.user and request.user.role == 'admin'

    def has_object_permission(self, request, view, obj):
        return request.user and request.user.role == 'admin'
