from rest_framework.permissions import BasePermission

class BlogPermission(BasePermission):
    def has_permission(self, request, view):
        if view.action == 'list':
            return True
        return False


class PostPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and view.action in ("create", "retrieve", "update", "destroy"):
            return True
        if view.action == 'list':
            return True
        if view.action == 'create':
            return True

        return False


    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser or request.user == obj