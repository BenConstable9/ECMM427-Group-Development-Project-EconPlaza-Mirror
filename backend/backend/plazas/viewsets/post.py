from rest_framework import viewsets, mixins, filters
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from utils import ActionBasedPermission
from utils import IsVerified
from utils import StandardResultsSetPagination

from ..serializers import PostSerializer
from ..models import Plaza, Post


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
        plaza = Plaza.objects.get(slug=self.kwargs["plazas_slug"])
        return Post.objects.filter(plaza=plaza.id)

    serializer_class = PostSerializer

    permission_classes = (ActionBasedPermission,)
    action_permissions = {
        IsVerified: ["create"],
        IsAuthenticated: ["retrieve", "list"],
        AllowAny: ["register_view"],
    }

    pagination_class = StandardResultsSetPagination

    lookup_field = "id"

    filter_backends = [filters.OrderingFilter]

    ordering_fields = [
        "id",
    ]

    ordering = ["id"]

    def perform_create(self, serializer):
        plaza = Plaza.objects.get(slug=self.kwargs["plazas_slug"])

        # Force the user to be the logged in user and the plaza to be from the slug
        serializer.save(user=self.request.user, plaza=plaza)

    @action(methods=["GET"], detail=True, url_path="view")
    def register_view(self, request, **kwargs):
        post = get_object_or_404(Post, id=kwargs["id"])
        post.views += 1
        post.save()
        return Response(PostSerializer(post).data)
