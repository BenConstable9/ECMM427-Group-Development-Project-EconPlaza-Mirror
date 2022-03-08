import json
from rest_framework.request import Request
from rest_framework.test import (
    APIRequestFactory,
    APITestCase,
    force_authenticate,
    APIClient,
)
from rest_framework import status
from django.contrib.auth import get_user_model

from plazas.models import Plaza, Member
from plazas.serializers import PlazaSerializer


class MembershipsViewsetTest(APITestCase):
    def setUp(self):
        """Initialise user instance, which creates a profile instance."""

        User = get_user_model()

        self.user_1 = User.objects.create(
            username="user_1",
            first_name="Test",
            last_name="User",
            email="admin@test.com",
            is_staff=False,
            verified=True,
        )

        self.plaza = Plaza.objects.create(
            name="Test Plaza", slug="Test", permissions="{}"
        )

        # Add one membership
        self.membership = Member.objects.create(
            user=self.user_1, plaza=self.plaza, member_type="MB"
        )

        self.client = APIClient()

    def test_get_members(self):
        """Test we get a HTTP 200 response when looking at list view."""
        self.client.force_authenticate(self.user_1)

        # Get some data
        response = self.client.get("/v1/users/{}/memberships/".format(self.user_1.id))

        factory = APIRequestFactory()
        request = factory.get("/v1/users/{}/memberships/".format(self.user_1.id))

        force_authenticate(request, user=self.user_1)

        serializer_context = {
            "request": Request(request),
        }

        serializer = PlazaSerializer(instance=self.plaza, context=serializer_context)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)
        self.assertEqual(response.data["results"][0], serializer.data)

    def test_get_members_unauth(self):
        """Test we get a HTTP 404 response when looking at list view."""

        # Get some data
        response = self.client.get("/v1/users/{}/memberships/".format(self.user_1.id))

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_member(self):
        """Test we get a HTTP 404 response when attempting to delete data."""
        self.client.force_authenticate(self.user_1)

        # Set the delete type
        response = self.client.delete(
            "/v1/users/{}/membership/{}/".format(self.user_1.id, self.membership.id)
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_member_unauth(self):
        """Test we get a HTTP 404 response when attempting to delete data and we aren't authorised."""

        # Set the delete type
        response = self.client.delete(
            "/v1/users/{}/membership/{}/".format(self.user_1.id, self.membership.id)
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_put_member(self):
        """Test we get a HTTP 404 response when attempting to update data."""
        self.client.force_authenticate(self.user_1)

        # Set the payload
        payload = {"user": 2}
        response = self.client.put(
            "/v1/users/{}/membership/{}/".format(self.user_1.id, self.membership.id),
            payload,
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_put_member_unauth(self):
        """Test we get a HTTP 404 response when attempting to update data and we aren't authorised."""
        # Set the payload
        payload = {"user": 2}
        response = self.client.put(
            "/v1/users/{}/membership/{}/".format(self.user_1.id, self.membership.id),
            payload,
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_post_member(self):
        """Test we get a HTTP 405 response when attempting to add data."""
        self.client.force_authenticate(self.user_1)

        # Set the payload
        payload = {
            "plaza": self.plaza.id,
            "user": self.user_1.id,
            "member_type": "MB",
        }

        response = self.client.post(
            "/v1/users/{}/membership/".format(self.user_1.id), payload
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_post_member_unauth(self):
        """Test we get a HTTP 403 response when attempting to add data as we aren't authorised."""

        # Set the payload
        payload = {
            "plaza": self.plaza.id,
            "user": self.user_1.id,
            "member_type": "MB",
        }

        response = self.client.post(
            "/v1/users/{}/membership/".format(self.user_1.id), payload
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
