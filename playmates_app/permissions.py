from rest_framework import permissions
from .models import Playmate



class IsAuthor(permissions.BasePermission):
    #Global permission check for adding Playmates

    def has_object_permission(self, request, view, obj):
            if request.method in permissions.SAFE_METHODS:
                return True

                
            return obj.author == request.user