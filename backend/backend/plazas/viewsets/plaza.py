from rest_framework import viewsets, filters, permissions

from utils import StandardResultsSetPagination

from ..serializers import PlazaSerializer
from ..models import Plaza


class PlazaViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to view Plazas
    """

    queryset = Plaza.objects.all()
    serializer_class = PlazaSerializer
    permission_classes = [permissions.IsAuthenticated]

    lookup_field = "slug"

    pagination_class = StandardResultsSetPagination

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["name", "description"]

    ordering_fields = [
        "id",
        "slug",
    ]
    ordering = ["id"]
