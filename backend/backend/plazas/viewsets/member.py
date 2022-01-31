from rest_framework import viewsets, mixins, filters
from rest_framework.permissions import IsAuthenticated

from utils import ActionBasedPermission
from utils import StandardResultsSetPagination

from ..serializers import MemberSerializer
from ..models import Plaza, Member


class MemberViewSet(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    """
    API endpoint that allows users to join a Plaza.
    """

    def get_queryset(self):
        plaza = Plaza.objects.get(slug=self.kwargs["plazas_slug"])
        return Member.objects.filter(plaza=plaza.id)

    serializer_class = MemberSerializer

    permission_classes = (ActionBasedPermission,)
    action_permissions = {
        IsAuthenticated: ["create"],
    }

    def perform_create(self, serializer):
        plaza = Plaza.objects.get(slug=self.kwargs["plazas_slug"])

        # Force the user to be the logged in user and the plaza to be from the slug
        serializer.save(user=self.request.user, plaza=plaza)
