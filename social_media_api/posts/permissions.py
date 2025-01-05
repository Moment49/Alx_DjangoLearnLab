from rest_framework import permissions

class CustomUserPerm(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        print("working perm")
        return obj.author == request.user