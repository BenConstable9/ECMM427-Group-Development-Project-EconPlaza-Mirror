from rest_framework.request import Request
from rest_framework.test import (
    APIRequestFactory,
    APITestCase,
    force_authenticate,
    APIClient,
)
from rest_framework import status
from django.contrib.auth import get_user_model

from ...serializers import UserSerializer
from ...views import AuthenticatedUserView


class AuthenticatedUserViewTest(APITestCase):
    def setUp(self):
        """Initialise user instance, which creates a profile instance."""

        User = get_user_model()
        self.user_1 = User.objects.create(username="user_1")
        self.user_1.set_password("password_1")
        self.user_1.save()

        self.client = APIClient()

    def test_get_user(self):
        """Test we get a HTTP 200 response when looking at detailed view."""

        User = get_user_model()

        # Now test the actual data is the same
        self.client.force_authenticate(self.user_1)
        response = self.client.get("/v1/users/me/")

        user = User.objects.get(id=self.user_1.id)

        factory = APIRequestFactory()
        request = factory.get("/v1/users/me/")

        serializer_context = {
            "request": Request(request),
        }

        serializer = UserSerializer(instance=user, context=serializer_context)

        # Check with the data direct from model
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_user_unauth(self):
        """Test we get a HTTP 401 response when looking at the view."""

        # Get some data
        response = self.client.get("/v1/users/me/")

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
