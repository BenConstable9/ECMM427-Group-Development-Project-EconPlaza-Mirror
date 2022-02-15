from rest_framework import viewsets, mixins, filters, permissions

from utils import StandardResultsSetPagination

from ..serializers import AvailableTagSerializer
from ..models import AvailableTag


class AvailableTagViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    """
    API endpoint that allows users to view Plazas
    """

    queryset = AvailableTag.objects.all()
    serializer_class = AvailableTagSerializer
    permission_classes = [permissions.IsAuthenticated]

    lookup_field = "name"

    pagination_class = StandardResultsSetPagination

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["name"]

    ordering_fields = [
        "id",
        "name",
    ]
    ordering = ["id"]
