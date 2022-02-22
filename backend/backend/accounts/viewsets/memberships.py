from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model

from plazas.serializers import PlazaSerializer
from plazas.models import Plaza

from utils import SmallResultsSetPagination


class MembershipViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    """
    API endpoint that allows the viewing of a specific plaza
    """

    def get_queryset(self):
        # If we aren't looking at ones self
        user = get_user_model().objects.get(id=self.kwargs["users_pk"])
        return Plaza.objects.filter(member__user=user)

    serializer_class = PlazaSerializer
    permission_classes = [IsAuthenticated]

    pagination_class = SmallResultsSetPagination
