from rest_framework import viewsets, mixins, permissions

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