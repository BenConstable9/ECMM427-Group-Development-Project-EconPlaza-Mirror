from rest_framework import viewsets, mixins, filters, permissions
from django.db.models import Count

from utils import LargeResultsSetPagination

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

    queryset = (
        AvailableTag.objects.all()
        .annotate(tag_count=Count("tag"))
        .order_by("-tag_count")
    )
    serializer_class = AvailableTagSerializer
    permission_classes = [permissions.IsAuthenticated]

    lookup_field = "name"

    pagination_class = LargeResultsSetPagination

    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]
