from rest_framework import viewsets

from ..serializers import PlazaSerializer
from ..models import Plaza


class PlazaViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to vouch for someone.
    """

    queryset = Plaza.objects.all()
    serializer_class = PlazaSerializer
