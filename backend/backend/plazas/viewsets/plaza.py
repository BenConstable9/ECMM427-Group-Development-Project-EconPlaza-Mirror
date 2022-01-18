from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from ..serializers import PlazaSerializer, PostSerializer
from ..models import Plaza, Post


class PlazaViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to view Plazas
    """

    queryset = Plaza.objects.all()
    serializer_class = PlazaSerializer
    lookup_field = "slug"
