import re

from rest_framework.permissions import SAFE_METHODS, AllowAny
from rest_framework.permissions import AllowAny, IsAuthenticated


# Taken form https://stackoverflow.com/questions/39392007/django-rest-framework-viewset-permissions-create-without-list


class ActionBasedPermission(AllowAny):
    """
    Grant or deny access to a view, based on a mapping in view.action_permissions
    """

    def has_permission(self, request, view):
        for klass, actions in getattr(view, "action_permissions", {}).items():
            if view.action in actions:
                return klass().has_permission(request, view)
        return False


class IsVerified(AllowAny):
    """
    Custom permission to only allow verified users to vouch.
    """

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            # Let through GET, HEAD and OPTIONS
            if request.method in SAFE_METHODS:
                return True
            else:
                # Check if verified
                return request.user.verified
        else:
            return False


class ContainsPlazaURL(AllowAny):
    """
    Custom permission that checks we are accessing /plazas/.
    """

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if re.search("\/plazas\/.*\/", request.path):
                return True

        return False


class ContainsPlazaURLVerified(AllowAny):
    """
    Custom permission that checks we are accessing /plazas/ and we are verified.
    """

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if re.search("\/plazas\/.*\/", request.path):
                # Check if verified
                return request.user.verified
        return False


class IsSelf(AllowAny):
    """Custom permission to only allow requests to /users/1/slug when the user is theirself"""

    def has_permission(self, request, view):
        return request.user.id == int(view.kwargs["users_pk"])
