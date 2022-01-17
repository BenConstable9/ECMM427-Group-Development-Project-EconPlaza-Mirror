from rest_framework.test import (
    APIRequestFactory,
    APITestCase,
    force_authenticate,
    APIClient,
)
from rest_framework.request import Request
from rest_framework import status
from django.contrib.auth import get_user_model
from ...models import Vouch
from ...serializers import VouchSerializer
from ...viewsets import VouchViewSet


class VouchViewsetTest(APITestCase):
    def setUp(self):
        """Initialise user instance, which creates a profile instance."""
        User = get_user_model()

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
        self.user_4 = User.objects.create(username="user_4")
        self.user_5 = User.objects.create(username="user_5")

        Vouch.objects.create(voucher=self.user_1, vouchee=self.user_3)
        Vouch.objects.create(voucher=self.user_2, vouchee=self.user_3)
        Vouch.objects.create(voucher=self.user_4, vouchee=self.user_3)
        Vouch.objects.create(voucher=self.user_5, vouchee=self.user_3)

        # Add some verifications for starting
        Vouch.objects.create(voucher=self.user_1, vouchee=self.user_2)
        Vouch.objects.create(voucher=self.user_2, vouchee=self.user_1)

        self.client = APIClient()

    def test_get_vouch(self):
        """Test we get a HTTP 200 response when looking at detailed view."""

        # Now test the actual data is the same
        self.client.force_authenticate(self.user_1)
        response = self.client.get(
            "/v1/users/{}/vouches/".format(self.user_2.id))

        factory = APIRequestFactory()
        request = factory.get("/v1/users/{}/vouches/".format(self.user_2.id))

        serializer_context = {
            "request": Request(request),
        }

        vouches = Vouch.objects.get(vouchee=self.user_2)
        serializer = VouchSerializer(vouches, context=serializer_context)

        # Check with the data direct from model
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0], serializer.data)
        self.assertIsInstance(response.data, list)

    def test_get_vouch_unauth(self):
        """Test we get a HTTP 401 response when looking at detailed view."""

        # Get some data
        response = self.client.get(
            "/v1/users/{}/vouches/".format(self.user_2.id))

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_vouch(self):
        """Test we get a HTTP 403 response when attempting to delete data."""
        self.client.force_authenticate(self.user_2)

        # Set the delete type
        response = self.client.delete(
            "/v1/users/{}/vouches/".format(self.user_2.id))

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_vouch_unauth(self):
        """Test we get a HTTP 401 response when attempting to delete data and we aren't authorised."""

        # Set the delete type
        response = self.client.delete(
            "/v1/users/{}/vouches/".format(self.user_2.id))

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_put_vouch(self):
        """Test we get a HTTP 403 response when attempting to update data."""
        self.client.force_authenticate(self.user_4)

        Vouch.objects.create(voucher=self.user_4, vouchee=self.user_2)

        # Set the payload
        payload = {"vouchee": self.user_2.id, "voucher": self.user_4.id}
        response = self.client.put(
            "/v1/users/{}/vouches/".format(self.user_2.id), payload
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_put_vouch_unauth(self):
        """Test we get a HTTP 401 response when attempting to update data and we aren't authorised."""
        Vouch.objects.create(voucher=self.user_5, vouchee=self.user_2)

        # Set the payload
        payload = {"vouchee": self.user_2.id, "voucher": self.user_5.id}
        response = self.client.put(
            "/v1/users/{}/vouches/".format(self.user_2.id), payload
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_post_vouch(self):
        """Test we get a HTTP 201 response when attempting to add data."""
        self.client.force_authenticate(self.user_3)

        # Set the payload
        payload = {"vouchee": self.user_2.id, "voucher": self.user_3.id}
        response = self.client.post(
            "/v1/users/{}/vouches/".format(self.user_2.id), payload)

        exists = Vouch.objects.filter(
            vouchee=self.user_2,
            voucher=self.user_3,
        ).exists()

        self.assertTrue(exists)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_vouch_with_unauth(self):
        """Test we get a HTTP 403 response when attempting to add data as we are not authorised."""
        self.client.force_authenticate(self.user_1)

        # Set the payload
        payload = {"vouchee": self.user_1.id, "voucher": self.user_3.id}
        response = self.client.post(
            "/v1/users/{}/vouches/".format(self.user_1.id), payload)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
