from datetime import timedelta
from django.db.models import Max
from django.utils import timezone
from rest_framework import viewsets, filters, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from utils import StandardResultsSetPagination

from ..serializers import PlazaSerializer
from ..models import Plaza, Post


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

    @action(methods=["GET"], detail=True, url_path="popular")
    def popular(self, request, **kwargs):
        two_weeks_ago = timezone.now().date() - timedelta(days=14)
        # Order by most popular post within a plaza, from the last two weeks
        plazas = (
            Post.objects.filter(created_at__gte=two_weeks_ago)
            .values("plaza", "plaza__name", "plaza__slug")
            .annotate(most_views=Max("views"))
            .order_by("-most_views")
        )
        if plazas.count() >= 5:
            print("More than 5")
            return Response(plazas, status=status.HTTP_200_OK)
        else:
            print("Less than 5")
            all_plazas = (
                Post.objects.values("plaza", "plaza__name", "plaza__slug")
                .annotate(most_views=Max("views"))
                .order_by("-most_views")
            )
            return Response(all_plazas, status=status.HTTP_200_OK)
