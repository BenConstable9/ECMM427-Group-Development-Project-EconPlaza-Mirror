from datetime import timedelta
from django.db.models import Max
from django.db.models.functions import Greatest
from django.utils import timezone
from rest_framework import viewsets, filters, permissions, status, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Max, Q
from itertools import chain

from utils import StandardResultsSetPagination

from ..serializers import PlazaSerializer
from ..models import Plaza, Post, Member, AvailableTag


class PlazaViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
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
        "name",
        "slug",
    ]
    ordering = ["slug"]

    def perform_create(self, serializer):
        sent_tags = self.request.data["tags"]
        tags_to_save = []
        for sent_tag in sent_tags:
            tags_to_save.append(AvailableTag.objects.get(id=sent_tag["ID"]))

        serializer.save(tags=tags_to_save)

    def list(self, request, *args, **kwargs):
        if "my" in request.GET:
            # If there is a get variable "my" /plazas/?my
            _NUMBER_OF_PLAZAS = 3
            # Get user's most recently interacted with plazas
            memberships = (
                Plaza.objects.filter(member__user=request.user)
                .annotate(
                    # Get most recent post in plaza by the user
                    most_recent_post=Max(
                        "post__created_at",
                        filter=Q(post__user=request.user),
                    ),
                    # Get most recent comment in plaza by the user
                    most_recent_comment=Max(
                        "post__comment__created_at",
                        filter=Q(post__comment__user=request.user),
                    ),
                    # Use the most recent datetime out of the two
                    most_recent_activity=Greatest(
                        "most_recent_post",
                        "most_recent_comment",
                    ),
                )
                .order_by(
                    # Order descending by most recent
                    "-most_recent_activity"
                )
            )
            if memberships.count() < _NUMBER_OF_PLAZAS:
                other_plazas = (
                    Plaza.objects.all()
                    .annotate(
                        # Get most recent post in plaza by any user
                        most_recent_post=Max(
                            "post__created_at",
                        ),
                        # Get most recent comment in plaza by any user
                        most_recent_comment=Max(
                            "post__comment__created_at",
                        ),
                        # Use the most recent datetime out of the two
                        most_recent_activity=Greatest(
                            "most_recent_post",
                            "most_recent_comment",
                        ),
                    )
                    .order_by(
                        # Order descending by most recent
                        "-most_recent_activity"
                    )[: _NUMBER_OF_PLAZAS - memberships.count()]
                )
                # Add the other plazas to the list
                memberships = list(chain(memberships, other_plazas))
            return Response(
                PlazaSerializer(
                    memberships[:_NUMBER_OF_PLAZAS],
                    many=True,
                    context={"request": request},
                ).data
            )
        # Return list as normal
        return super().list(request)

    @action(methods=["GET"], detail=True, url_path="popular")
    def popular(self, request, **kwargs):
        two_weeks_ago = timezone.now() - timedelta(days=14)
        # Order by most popular post within a plaza, from the last two weeks
        plazas = (
            Post.objects.filter(created_at__gte=two_weeks_ago)
            .values("plaza", "plaza__name", "plaza__slug")
            .annotate(most_views=Max("views"))
            .order_by("-most_views")
        )
        if plazas.count() >= 5:
            return Response(plazas, status=status.HTTP_200_OK)
        else:
            all_plazas = (
                Post.objects.values("plaza", "plaza__name", "plaza__slug")
                .annotate(most_views=Max("views"))
                .order_by("-most_views")
            )
            return Response(all_plazas, status=status.HTTP_200_OK)
