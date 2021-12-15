from rest_framework.test import APIRequestFactory, APITestCase, force_authenticate, APIClient
from rest_framework import status

from ...models import Vouch, User
from ...serializers import VouchSerializer
from ...viewsets import VouchViewSet

class VouchViewsetTest(APITestCase):
    def setUp(self):
        """Initialise user instance, which creates a profile instance."""
        self.user_1 = User.objects.create(username="user_1")

        self.user_2 = User.objects.create(username="user_2")

        self.user_3 = User.objects.create(username="user_3", verified=1)

        Vouch.objects.create(voucher=self.user_1, vouchee=self.user_2)
        Vouch.objects.create(voucher=self.user_2, vouchee=self.user_1)

        self.client = APIClient()

    def test_get_vouches(self):
        """Test we get a HTTP 200 response when looking at the list view."""
        factory = APIRequestFactory()
        view = VouchViewSet.as_view({'get': 'list'})

        # Make an authenticated request to the view...
        request = factory.get('/accounts/vouches/')
        force_authenticate(request, user=self.user_1)
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Now test the actual data is the same
        self.client.force_authenticate(self.user_1)
        response = self.client.get('/accounts/vouches/')

        vouches = Vouch.objects.all()
        serializer = VouchSerializer(vouches, many=True)

        # Check with the data direct from model
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_vouch(self):
        """Test we get a HTTP 200 response when looking at the detailed view."""
        factory = APIRequestFactory()
        view = VouchViewSet.as_view({'get': 'retrieve'})

        # Make an authenticated request to the view...
        request = factory.get('/accounts/vouches/')
        force_authenticate(request, user=self.user_1)
        response = view(request, vouchee=self.user_1.id)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_vouch(self):
        """Test we get a HTTP 405 response when attempting to delete data."""
        factory = APIRequestFactory()
        view = VouchViewSet.as_view({'delete': 'retrieve'})

        # Make an authenticated request to the view...
        request = factory.get('/accounts/vouches/')
        force_authenticate(request, user=self.user_1)
        response = view(request, vouchee=self.user_1.id)

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_put_vouch(self):
        """Test we get a HTTP 403 response when attempting to update data."""
        self.client.force_authenticate(self.user_2)

        # Set the payload
        payload = {'vouchee': self.user_3.id, 'voucher': self.user_2.id}
        response = self.client.put('/accounts/vouches/'.format(self.user_3.id), payload)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_vouch(self):
        """Test we get a HTTP 201 response when attempting to add data."""
        self.client.force_authenticate(self.user_3)

        # Set the payload
        payload = {'vouchee': self.user_2.id, 'voucher': self.user_3.id}
        response = self.client.post('/accounts/vouches/', payload)

        exists = Vouch.objects.filter(
            vouchee = self.user_2,
            voucher = self.user_3,
        ).exists()

        self.assertTrue(exists)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_unathorised_vouch(self):
        """Test we get a HTTP 403 response when looking at the detailed view as we aren't authenticated."""
        factory = APIRequestFactory()
        view = VouchViewSet.as_view({'get': 'retrieve'})

        # Don't authenticate this request
        request = factory.get('/accounts/vouches/')
        response = view(request, vouchee=self.user_1.id)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_invalid_vouch(self):
        """Test we get a HTTP 404 response when looking at the detailed view."""
        factory = APIRequestFactory()
        view = VouchViewSet.as_view({'get': 'retrieve'})

        # Make an authenticated request to the view...
        request = factory.get('/accounts/vouches/')
        force_authenticate(request, user=self.user_1)

        # Use an invalid id
        response = view(request, vouchee=200)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)