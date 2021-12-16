from rest_framework import viewsets, mixins, permissions, filters

from utils import StandardResultsSetPagination

from ..serializers import UserSerializer
from ..models import User

# Only allow GET, HEAD and OPTIONS requests
class UserViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    API endpoint that allows for viewing of users.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    pagination_class = StandardResultsSetPagination

    # Add a search filter
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['username', 'email', 'first_name', 'last_name']

    ordering_fields = ['id', 'username', 'email', 'first_name', 'last_name', 'date_joined']
    ordering = ['id']