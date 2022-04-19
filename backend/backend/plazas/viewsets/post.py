from rest_framework import viewsets, mixins, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from django.core.cache import cache
from plazas.models.availabletag import AvailableTag

from django.db.models import Count, Max

from utils import ActionBasedPermission
from utils import (
    ContainsPlazaURLVerified,
    ContainsPlazaURL,
    ContainsPlazaURLVerifiedMember,
)
from utils import StandardResultsSetPagination

from ..serializers import PostSerializer
from ..models import Plaza, Post, AvailableTag
from hashlib import md5


class PostViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    """
    API endpoint that allows users to view Posts and create new ones
    """

    def get_queryset(self):
        available_tag_param = self.request.query_params.get("tag", None)

        # Need to annotate so that we can use replies in ordering
        # https://stackoverflow.com/questions/30041948/django-rest-framework-ordering-on-a-serializermethodfield
        posts = (
            Post.objects.annotate(replies=Count("comment__post"))
            .annotate(last_activity=Max("comment__created_at"))
            .all()
        )

        if available_tag_param:
            available_tag = get_object_or_404(AvailableTag, name=available_tag_param)
            posts = posts.filter(tags__tag=available_tag)
        if "plazas_slug" in self.kwargs:
            plaza = Plaza.objects.get(slug=self.kwargs["plazas_slug"])
            posts = posts.filter(plaza=plaza.id)
        return posts

    serializer_class = PostSerializer

    permission_classes = (ActionBasedPermission,)

    action_permissions = {
        ContainsPlazaURLVerifiedMember: ["create"],
        ContainsPlazaURLVerified: ["register_view"],
        ContainsPlazaURL: ["retrieve"],
        IsAuthenticated: ["list"],
    }

    pagination_class = StandardResultsSetPagination

    lookup_field = "id"

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["title"]

    ordering_fields = ["id", "views", "replies", "last_activity"]

    ordering = ["-id"]

    def perform_create(self, serializer):
        plaza = Plaza.objects.get(slug=self.kwargs["plazas_slug"])

        # Build our list of tags to send
        sent_tags = self.request.data["tags"]
        tags_to_save = []
        for sent_tag in sent_tags:
            tags_to_save.append(AvailableTag.objects.get(id=sent_tag["ID"]))

        # Force the user to be the logged in user and the plaza to be from the slug
        serializer.save(user=self.request.user, plaza=plaza, tags=tags_to_save)

    @action(methods=["POST"], detail=True, url_path="view")
    def register_view(self, request, **kwargs):
        # Hash user IP with post id
        ip = request.META.get(
            "HTTP_X_FORWARDED_FOR", request.META.get("REMOTE_ADDR")
        ).split(",")[0]
        hash = md5(f"{ip}${kwargs['id']}".encode()).hexdigest()

        # Check if hash exists in cache
        if cache.get(hash):
            # If hash exists, user has already contributed to the view counter
            return Response()
        # If user has not viewed the post already, create cache entry and increment view count
        cache.set(hash, True, 60 * 15)  # Cache will expire in 15 mins
        post = get_object_or_404(Post, id=kwargs["id"])
        post.views += 1
        post.save()
        return Response()
