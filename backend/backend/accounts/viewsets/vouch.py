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


class VouchViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    """
    API endpoint that allows users to vouch for someone.
    """

    def get_queryset(self):
        user = get_user_model().objects.get(id=self.kwargs["users_pk"])
        return Vouch.objects.filter(vouchee=user)

    serializer_class = VouchSerializer

    # Allow different permissions based on the action
    # Taken from https://stackoverflow.com/questions/39392007/django-rest-framework-viewset-permissions-create-without-list
    permission_classes = (ActionBasedPermission,)
    action_permissions = {IsVerified: ["create"], IsAuthenticated: ["list"]}

    def perform_create(self, serializer):
        # Force the vouchee to be the same user as url
        vouchee = get_user_model().objects.get(id=self.kwargs["users_pk"])

        # Force the voucher to be the logged in user
        serializer.save(voucher=self.request.user, vouchee=vouchee)
