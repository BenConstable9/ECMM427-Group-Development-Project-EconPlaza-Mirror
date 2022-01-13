from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from utils import ActionBasedPermission
from utils import IsVerified

from ..serializers import VouchSerializer
from ..models import Vouch

# Only allow POST, GET, HEAD and OPTIONS requests
# Need to inherit list although we block it.


class VouchViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    API endpoint that allows users to vouch for someone.
    """

    queryset = Vouch.objects.all()
    serializer_class = VouchSerializer

    # Allow different permissions based on the action
    # Taken from https://stackoverflow.com/questions/39392007/django-rest-framework-viewset-permissions-create-without-list
    permission_classes = (ActionBasedPermission,)
    action_permissions = {
        IsVerified: ['create'],
        IsAuthenticated: ['retrieve']
    }

    # Ensures we look up against the vouchee field on a retrieve mixin
    lookup_field = 'vouchee'

    def perform_create(self, serializer):
        # Force the voucher to be the logged in user
        serializer.save(voucher=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        # Overwrite the retrieve functionality to allow us to return more than one result
        vouchee_id = kwargs.get('vouchee', None)

        # Ensure we force a 404 if the user doesn't actually exist
        vouchee = get_object_or_404(get_user_model(), pk=vouchee_id)

        self.queryset = Vouch.objects.filter(vouchee=vouchee)
        return super(VouchViewSet, self).list(request, *args, **kwargs)
