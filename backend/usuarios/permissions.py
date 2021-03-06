from django.contrib.auth.models import AnonymousUser
from rest_framework import permissions

class IsUserOrAdmin(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        if type(request.user) is not AnonymousUser:
            if str(request.user.rol) == 'Administrador' or request.user.is_staff:
                return True
            # Instance must have an attribute named `owner`.
            return obj == request.user
        return False