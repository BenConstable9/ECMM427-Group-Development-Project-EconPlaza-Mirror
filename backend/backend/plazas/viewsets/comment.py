from rest_framework import viewsets, mixins, filters
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from utils import ActionBasedPermission
from utils import IsVerified
from utils import StandardResultsSetPagination

from ..serializers import CommentSerializer
from ..models import Plaza, Post, Comment


class CommentViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    """
    API endpoint that allows users to view Comments and create new ones
    """

    def get_queryset(self):
        plaza = Plaza.objects.get(slug=self.kwargs["plazas_slug"])
        post = Post.objects.get(id=self.kwargs["posts_id"], plaza=plaza.id)
        return Comment.objects.filter(post=post.id)

    serializer_class = CommentSerializer

    permission_classes = (ActionBasedPermission,)
    action_permissions = {IsVerified: ["create"], IsAuthenticated: ["list", "retrieve"]}

    lookup_field = "id"

    pagination_class = StandardResultsSetPagination

    # Add a search filter
    filter_backends = [filters.OrderingFilter]

    ordering_fields = [
        "id",
    ]
    ordering = ["-id"]

    def perform_create(self, serializer):
        plaza = Plaza.objects.get(slug=self.kwargs["plazas_slug"])
        post = Post.objects.get(id=self.kwargs["posts_id"], plaza=plaza.id)

        # Force the user to be the logged in user and the post from the URL
        serializer.save(user=self.request.user, post=post)
