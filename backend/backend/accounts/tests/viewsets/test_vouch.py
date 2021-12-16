from rest_framework.test import APIRequestFactory, APITestCase, force_authenticate, APIClient
from rest_framework import status

from ...models import Vouch, User
from ...serializers import VouchSerializer
from ...viewsets import VouchViewSet

class VouchViewsetTest(APITestCase):
    def setUp(self):
        """Initialise user instance, which creates a profile instance."""
        self.user_1 = User.objects.create(username="user_1")
        self.user_1.set_password("password_1")
        self.user_1.save()

        self.user_2 = User.objects.create(username="user_2")
        self.user_2.set_password("password_2")
        self.user_2.save()

        self.user_3 = User.objects.create(username="user_3", verified=1)
        self.user_3.set_password("password_3")
        self.user_3.save()

        # Have to manually verify user 3 so they can verify
        user_4 = User.objects.create(username="user_4")
        user_5 = User.objects.create(username="user_5")
        
        self.staff_user = User.objects.create(username="staff_user", is_staff=True)

        Vouch.objects.create(voucher=self.user_1, vouchee=self.user_3)
        Vouch.objects.create(voucher=self.user_2, vouchee=self.user_3)
        Vouch.objects.create(voucher=user_4, vouchee=self.user_3)
        Vouch.objects.create(voucher=user_5, vouchee=self.user_3)
        Vouch.objects.create(voucher=self.staff_user, vouchee=self.user_3)

        # Add some verifications for starting
        Vouch.objects.create(voucher=self.user_1, vouchee=self.user_2)
        Vouch.objects.create(voucher=self.user_2, vouchee=self.user_1)

        self.client = APIClient()

    def test_get_vouch(self):
        """Test we get a HTTP 200 response when looking at detailed view."""

        # Now test the actual data is the same
        self.client.force_authenticate(self.user_1)
        response = self.client.get('/accounts/vouches/{}/'.format(self.user_2.id))

        vouches = Vouch.objects.get(vouchee=self.user_2)
        serializer = VouchSerializer(vouches)

        # Check with the data direct from model
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_vouch_unauth(self):
        """Test we get a HTTP 403 response when looking at detailed view."""

        # Get some data
        response = self.client.get('/accounts/vouches/{}/'.format(self.user_2.id))

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_vouches_unauth(self):
        """Test we get a HTTP 403 response when looking at list view."""

        # Get some data
        response = self.client.get('/accounts/vouches/')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_vouches(self):
        """Test we get a HTTP 403 response when looking at list view."""

        # Get some data
        self.client.force_authenticate(self.user_1)
        response = self.client.get('/accounts/vouches/')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_vouch(self):
        """Test we get a HTTP 405 response when attempting to delete data."""
        self.client.force_authenticate(self.user_2)

        # Set the delete type
        response = self.client.delete('/accounts/vouches/'.format(self.user_2.id))

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_vouch_unauth(self):
        """Test we get a HTTP 405 response when attempting to delete data and we aren't authorised."""

        # Set the delete type
        response = self.client.delete('/accounts/vouches/'.format(self.user_2.id))

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_put_vouch(self):
        """Test we get a HTTP 403 response when attempting to update data."""
        self.client.force_authenticate(self.user_2)

        # Set the payload
        payload = {'vouchee': self.user_3.id, 'voucher': self.user_2.id}
        response = self.client.put('/accounts/vouches/'.format(self.user_3.id), payload)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_put_vouch_unauth(self):
        """Test we get a HTTP 403 response when attempting to update data and we aren't authorised."""
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

    def test_post_vouch_with_staff(self):
        """Test we get a HTTP 201 response when attempting to add data as we are staff."""
        self.client.force_authenticate(self.staff_user)

        # Set the payload
        payload = {'vouchee': self.user_2.id, 'voucher': self.staff_user.id}
        response = self.client.post('/accounts/vouches/', payload)

        exists = Vouch.objects.filter(
            vouchee = self.user_2,
            voucher = self.staff_user,
        ).exists()

        self.assertTrue(exists)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_vouch_with_unauth(self):
        """Test we get a HTTP 403 response when attempting to add data as we are not authorised."""
        self.client.force_authenticate(self.user_1)

        # Set the payload
        payload = {'vouchee': self.user_1.id, 'voucher': self.user_3.id}
        response = self.client.post('/accounts/vouches/', payload)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

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