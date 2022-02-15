from datetime import timedelta
from django.db.models import Max
from django.utils import timezone
from rest_framework import viewsets, filters, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from utils import StandardResultsSetPagination

from ..serializers import AvailableTagSerializer
from ..models import AvailableTag


class AvailableTagViewSet(viewsets.ReadOnlyModelViewSet):
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
