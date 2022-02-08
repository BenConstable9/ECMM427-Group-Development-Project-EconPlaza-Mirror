from rest_framework import viewsets, mixins, permissions, filters
from rest_framework.permissions import SAFE_METHODS
from django.contrib.auth import get_user_model
from utils import StandardResultsSetPagination

from ..serializers import UserSerializer, UserPostSerializer
from ..permissions.create_or_authenticate import IsCreationOrIsAuthenticated

# Only allow GET, HEAD and OPTIONS requests


class UserViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    """
    API endpoint that allows for viewing and creating of users.
    """

    queryset = get_user_model().objects.all()

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return UserSerializer
        else:
            return UserPostSerializer

    permission_classes = [IsCreationOrIsAuthenticated]

    pagination_class = StandardResultsSetPagination

    # Add a search filter
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["username", "email", "first_name", "last_name"]

    ordering_fields = [
        "id",
        "username",
        "email",
        "first_name",
        "last_name",
        "date_joined",
    ]
    ordering = ["id"]
