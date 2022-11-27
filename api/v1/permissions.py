from rest_framework.permissions import BasePermission

from user.models import UserRoleChoices


class AdminPermission(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return request.user.role == UserRoleChoices.ADMIN


class SingerPermission(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return request.user.role == UserRoleChoices.SINGER


class ListenerPermission(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return request.user.role == UserRoleChoices.LISTENER
