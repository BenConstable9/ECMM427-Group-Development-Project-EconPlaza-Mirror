from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model

from plazas.serializers import PostSerializer
from plazas.models import Post


class ActivityViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    """
    API endpoint that allows the viewing of a specific plaza
    """

    def get_queryset(self):
        # If we aren't looking at ones self
        user = get_user_model().objects.get(id=self.kwargs["users_pk"])
        return Post.objects.filter(user=user, profile__global_anonymous=False).order_by(
            "-created_at"
        )[:15]

    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
