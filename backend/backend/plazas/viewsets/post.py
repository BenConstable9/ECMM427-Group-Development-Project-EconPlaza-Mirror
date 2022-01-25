from rest_framework import viewsets, mixins, filters
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from django.core.cache import cache

from utils import ActionBasedPermission
from utils import IsVerified
from utils import StandardResultsSetPagination

from ..serializers import PostSerializer
from ..models import Plaza, Post
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

    ordering = ["-id"]

    def perform_create(self, serializer):
        plaza = Plaza.objects.get(slug=self.kwargs["plazas_slug"])

        # Force the user to be the logged in user and the plaza to be from the slug
        serializer.save(user=self.request.user, plaza=plaza)

    @action(methods=["POST"], detail=True, url_path="view")
    def register_view(self, request, **kwargs):
        # Hash user IP with post id
        ip = request.META.get('HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR')).split(',')[0]
        hash = md5(f"{ip}${kwargs['id']}".encode()).hexdigest()

        print(hash)

        # Check if hash exists in cache
        if cache.get(hash):
            print("hash exists")
            # If hash exists, user has already contributed to the view counter
            return Response()
        print("hash does not exist")
        # If user has not viewed the post already, create cache entry and increment view count
        cache.set(hash, True, 60 * 15)  # Cache will expire in 15 mins
        post = get_object_or_404(Post, id=kwargs["id"])
        post.views += 1
        post.save()
        return Response()
