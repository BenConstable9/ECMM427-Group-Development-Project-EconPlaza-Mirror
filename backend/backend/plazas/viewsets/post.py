from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated

from utils import ActionBasedPermission
from utils import IsVerified

from ..serializers import PostSerializer
from ..models import Plaza, Post


class PostViewSet(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet,):
    """
    API endpoint that allows users to view Posts and create new ones
    """

    def get_queryset(self):
        plaza = Plaza.objects.get(slug=self.kwargs['plazas_slug'])
        return Post.objects.filter(plaza=plaza.id)

    serializer_class = PostSerializer

    permission_classes = (ActionBasedPermission,)
    action_permissions = {IsVerified: [
        "create"], IsAuthenticated: ["retrieve", "list"]}

    lookup_field = "slug"

    def perform_create(self, serializer):
        plaza = Plaza.objects.get(slug=self.kwargs['plazas_slug'])

        # Force the user to be the logged in user and the plaza to be from the slug
        serializer.save(user=self.request.user, plaza=plaza)
