from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model

from ..serializers import ProfileSerializer
from ..models import Profile


class ProfileViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    """
    API endpoint that allows the viewing of a specific plaza
    """

    def get_queryset(self):
        user = get_user_model().objects.get(id=self.kwargs["users_pk"])
        return Profile.objects.filter(user=user)

    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]
