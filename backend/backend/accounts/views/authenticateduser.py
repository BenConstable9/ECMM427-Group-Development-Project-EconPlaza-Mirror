from ..viewsets import UserViewSet
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response

from ..serializers import UserSerializer


class AuthenticatedUserView(APIView):
    """
    Retrieve the current authenticated user for JWT.
    """

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        serializer = UserSerializer(request.user, context={'request': request})
        return Response(serializer.data)
