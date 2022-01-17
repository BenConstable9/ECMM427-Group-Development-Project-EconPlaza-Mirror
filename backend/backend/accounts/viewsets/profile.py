from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated

from ..serializers import ProfileSerializer
from ..models import Profile


class ProfileViewSet(mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet,):
    """
    API endpoint that allows the viewing of a specific plaza
    """

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]
