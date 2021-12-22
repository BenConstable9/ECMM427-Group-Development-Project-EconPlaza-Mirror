from rest_framework.permissions import SAFE_METHODS, AllowAny

from ..models import User


class IsAdminOrVerified(AllowAny):
    """
    Custom permission to only allow verified users to vouch.
    """

    def has_permission(self, request, view):
        # Let through GET, HEAD and OPTIONS
        if request.method in SAFE_METHODS:
            return True
        else:
            # Check if verified

            return request.user.is_staff or request.user.verified
