from datetime import timedelta, datetime
from django.db.models import Max, F, ExpressionWrapper, DateTimeField
from django.db.models.functions import Greatest, Coalesce
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
            return self.get_my_plazas(request, *args, **kwargs)
        elif "popular" in request.GET:
            # If there is a get variable "popular" /plazas/?popular
            return self.get_popular_plazas(request, *args, **kwargs)
        # Return list as normal
        return super().list(request)

    @staticmethod
    def get_my_plazas(request, *args, **kwargs):
        _NUMBER_OF_PLAZAS = 3
        # Get user's most recently interacted with plazas
        memberships = (
            Plaza.objects.filter(member__user=request.user)
                .annotate(
                # Get most recent post in plaza by the user
                # We Coalesce with a 0 datetime as sqLite requires a non-null
                # value for the Greatest annotation used later. (this is not required for postgres)
                # https://docs.djangoproject.com/en/3.2/ref/models/database-functions/#greatest
                most_recent_post=Coalesce(Max(
                    "post__created_at",
                    filter=Q(post__user=request.user),
                ), datetime.utcfromtimestamp(0)),
                # Get most recent comment in plaza by the user
                most_recent_comment=Coalesce(Max(
                    "post__comment__created_at",
                    filter=Q(post__comment__user=request.user),
                ), datetime.utcfromtimestamp(0)),
                # Use the most recent datetime out of the two
                most_recent_activity=Greatest(
                    "most_recent_post",
                    "most_recent_comment",
                )
            ).order_by(
                # Order descending by most recent
                "-most_recent_activity"
            )
        )
        if memberships.count() < _NUMBER_OF_PLAZAS:
            other_plazas = (
                Plaza.objects.all()
                    .annotate(
                    # Get most recent post in plaza by any user
                    most_recent_post=Coalesce(Max(
                        "post__created_at",
                    ), datetime.utcfromtimestamp(0)),
                    # Get most recent comment in plaza by any user
                    most_recent_comment=Coalesce(Max(
                        "post__comment__created_at",
                    ), datetime.utcfromtimestamp(0)),
                    # Use the most recent datetime out of the two
                    most_recent_activity=Greatest(
                        "most_recent_post",
                        "most_recent_comment",
                    ),
                ).exclude(
                    pk__in=memberships
                ).order_by(
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

    @staticmethod
    def get_popular_plazas(request, *args, **kwargs):
        _NUMBER_OF_PLAZAS = 3
        two_weeks_ago = timezone.now() - timedelta(days=14)
        # Order by most popular post within a plaza, from the last two weeks
        plazas = Plaza.objects.filter(
            post__created_at__gte=two_weeks_ago,
        ).annotate(
            views=Max("post__views"),
        ).order_by("-views")

        if plazas.count() < _NUMBER_OF_PLAZAS:
            historically_popular_plazas = Plaza.objects.all().exclude(
                id__in=plazas,
            ).annotate(
                views=Max("post__views"),
            ).order_by("-views")
            plazas = list(chain(plazas, historically_popular_plazas))
        return Response(
            PlazaSerializer(
                plazas[:_NUMBER_OF_PLAZAS],
                many=True,
                context={"request": request},
            ).data
        )
