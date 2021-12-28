from rest_framework.request import Request
from rest_framework.test import APIRequestFactory, APITestCase, force_authenticate, APIClient
from rest_framework import status
from django.contrib.auth import get_user_model

from ...models import Profile
from ...serializers import UserSerializer
from ...viewsets import UserViewSet


class UserViewsetTest(APITestCase):
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
        response = self.client.get(
            '/v1/accounts/users/{}/'.format(self.user_1.id))

        user = User.objects.get(id=self.user_1.id)

        factory = APIRequestFactory()
        request = factory.get('/v1/accounts/users')

        serializer_context = {
            'request': Request(request),
        }

        serializer = UserSerializer(instance=user, context=serializer_context)

        # Check with the data direct from model
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_users_unauth(self):
        """Test we get a HTTP 401 response when looking at detailed view."""

        # Get some data
        response = self.client.get('/v1/accounts/users/')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_user_unauth(self):
        """Test we get a HTTP 401 response when looking at list view."""

        # Get some data
        response = self.client.get(
            '/v1/accounts/users/{}/'.format(self.user_1.id))

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_users(self):
        """Test we get a HTTP 200 response when looking at list view."""

        # Get some data
        self.client.force_authenticate(self.user_1)
        response = self.client.get('/v1/accounts/users/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)
        self.assertEqual(response.data["results"]
                         [0]["username"], self.user_1.username)
        self.assertEqual(response.data["results"][0]["id"], self.user_1.id)

    def test_get_users_invalid_search(self):
        """Test we get a HTTP 200 response when looking at list view."""

        # Get some data
        self.client.force_authenticate(self.user_1)
        response = self.client.get('/v1/accounts/users/?search=no')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 0)
        self.assertEqual(len(response.data["results"]), 0)

    def test_get_users_valid_search(self):
        """Test we get a HTTP 200 response when looking at list view."""
        User = get_user_model()

        # Add additional user
        user_2 = User.objects.create(username="user_2")

        # Get some data
        self.client.force_authenticate(self.user_1)
        response = self.client.get('/v1/accounts/users/?search=user_2')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)
        self.assertEqual(response.data["results"]
                         [0]["username"], user_2.username)
        self.assertEqual(response.data["results"][0]["id"], user_2.id)

        # Now delete them
        Profile.objects.filter(user_id=user_2.id).delete()
        User.objects.filter(id=user_2.id).delete()

    def test_delete_user(self):
        """Test we get a HTTP 405 response when attempting to delete data."""
        self.client.force_authenticate(self.user_1)

        # Set the delete type
        response = self.client.delete(
            '/v1/accounts/users/{}/'.format(self.user_1.id))

        self.assertEqual(response.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_delete_user_unauth(self):
        """Test we get a HTTP 401 response when attempting to delete data and we aren't authorised."""

        # Set the delete type
        response = self.client.delete(
            '/v1/accounts/users/{}/'.format(self.user_1.id))

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_put_user(self):
        """Test we get a HTTP 405 response when attempting to update data."""
        self.client.force_authenticate(self.user_1)

        # Set the payload
        payload = {'first_name': 'test2'}
        response = self.client.put(
            '/v1/accounts/users/{}/'.format(self.user_1.id), payload)

        self.assertEqual(response.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_put_user_unauth(self):
        """Test we get a HTTP 401 response when attempting to update data and we aren't authorised."""
        # Set the payload
        payload = {'first_name': 'test2'}
        response = self.client.put(
            '/v1/accounts/users/{}/'.format(self.user_1.id), payload)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_post_user(self):
        """Test we get a HTTP 405 response when attempting to add data."""
        self.client.force_authenticate(self.user_1)

        # Set the payload
        payload = {'first_name': 'tester', 'username': 'test'}
        response = self.client.post('/v1/accounts/users/', payload)

        self.assertEqual(response.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_post_vouch_with_unauth(self):
        """Test we get a HTTP 401 response when attempting to add data as we are not authorised."""

        # Set the payload
        payload = {'first_name': 'tester', 'username': 'test'}
        response = self.client.post('/v1/accounts/users/', payload)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_invalid_user(self):
        """Test we get a HTTP 404 response when looking at the detailed view."""
        factory = APIRequestFactory()
        view = UserViewSet.as_view({'get': 'retrieve'})

        # Make an authenticated request to the view...
        request = factory.get('/v1/accounts/users/')
        force_authenticate(request, user=self.user_1)

        # Use an invalid id
        response = view(request, pk=200)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
