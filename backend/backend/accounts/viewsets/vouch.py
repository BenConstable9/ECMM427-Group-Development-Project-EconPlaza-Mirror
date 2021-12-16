from rest_framework import viewsets, mixins, permissions
from rest_framework.permissions import IsAuthenticated

from utils import ActionBasedPermission

from ..permissions import IsAdminOrVerified
from ..serializers import VouchSerializer
from ..models import Vouch

# Only allow POST, GET, HEAD and OPTIONS requests
class VouchViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    API endpoint that allows users to vouch for someone.
    """

    queryset = Vouch.objects.all()
    serializer_class = VouchSerializer
    #permission_classes = [permissions.IsAuthenticated, IsAdminOrVerified]

    # Allow different permissions based on the action
    # Taken from https://stackoverflow.com/questions/39392007/django-rest-framework-viewset-permissions-create-without-list
    permission_classes = (ActionBasedPermission,)
    action_permissions = {
        IsAdminOrVerified: ['create'],
        IsAuthenticated: ['retrieve']
    }

    # Ensures we look up against the vouchee field on a retrieve mixin
    lookup_field = 'vouchee'

    def perform_create(self, serializer):
        # Force the voucher to be the logged in user
        serializer.save(voucher=self.request.user)