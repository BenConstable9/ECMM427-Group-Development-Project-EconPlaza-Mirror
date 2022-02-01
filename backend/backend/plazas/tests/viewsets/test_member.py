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

from ...models import Plaza, Member
from ...serializers import PlazaSerializer


class MemberViewsetTest(APITestCase):
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

        self.user_2 = User.objects.create(
            username="user_2",
            first_name="Test",
            last_name="User",
            email="admin2@test.com",
            is_staff=False,
            verified=True,
        )

        self.user_3 = User.objects.create(
            username="user_3",
            first_name="Test",
            last_name="User",
            email="admin3@test.com",
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
        """Test we get a HTTP 404 response when looking at list view."""
        self.client.force_authenticate(self.user_1)

        # Get some data
        response = self.client.get("/v1/plazas/{}/membership/".format(self.plaza.slug))

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_members_unauth(self):
        """Test we get a HTTP 404 response when looking at list view."""

        # Get some data
        response = self.client.get("/v1/plazas/{}/membership/".format(self.plaza.slug))

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_member(self):
        """Test we get a HTTP 404 response when attempting to delete data."""
        self.client.force_authenticate(self.user_1)

        # Set the delete type
        response = self.client.delete(
            "/v1/plazas/{}/membership/{}/".format(self.plaza.slug, self.membership.id)
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_member_unauth(self):
        """Test we get a HTTP 404 response when attempting to delete data and we aren't authorised."""

        # Set the delete type
        response = self.client.delete(
            "/v1/plazas/{}/membership/{}/".format(self.plaza.slug, self.membership.id)
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_put_member(self):
        """Test we get a HTTP 404 response when attempting to update data."""
        self.client.force_authenticate(self.user_1)

        # Set the payload
        payload = {"title": "test2"}
        response = self.client.put(
            "/v1/plazas/{}/membership/{}/".format(self.plaza.slug, self.membership.id),
            payload,
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_put_member_unauth(self):
        """Test we get a HTTP 404 response when attempting to update data and we aren't authorised."""
        # Set the payload
        payload = {"title": "test2"}
        response = self.client.put(
            "/v1/plazas/{}/membership/{}/".format(self.plaza.slug, self.membership.id),
            payload,
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_post_member(self):
        """Test we get a HTTP 201 response when attempting to add data."""
        self.client.force_authenticate(self.user_2)

        # Set the payload
        payload = {
            "plaza": self.plaza.id,
            "user": self.user_2.id,
            "member_type": "MB",
        }

        response = self.client.post(
            "/v1/plazas/{}/membership/".format(self.plaza.slug), payload
        )

        exists = Member.objects.filter(
            plaza=self.plaza,
            user=self.user_2,
        ).exists()

        self.assertTrue(exists)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_member_unauth(self):
        """Test we get a HTTP 403 response when attempting to add data as we aren't authorised."""

        # Set the payload
        payload = {
            "plaza": self.plaza.id,
            "user": self.user_2.id,
            "member_type": "MB",
        }

        response = self.client.post(
            "/v1/plazas/{}/membership/".format(self.plaza.slug), payload
        )

        exists = Member.objects.filter(
            plaza=self.plaza,
            user=self.user_2,
        ).exists()

        self.assertFalse(exists)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_post_member_duplicate(self):
        """Test we get a HTTP 401 response when attempting to add data as we are not authorised."""

        # Set the payload
        payload = {
            "plaza": self.plaza.id,
            "user": self.user_1.id,
            "member_type": "MB",
        }
        response = self.client.post(
            "/v1/plazas/{}/membership/".format(self.plaza.slug), payload
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
