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

from ...models import Profile

from plazas.models import Plaza, Member, Post
from plazas.serializers import PostSerializer


class ActivityViewsetTest(APITestCase):
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

        self.profile_1 = Profile.objects.create(
            user=self.user_1,
            display_name="tester",
            global_anonymous=False,
        )

        self.plaza = Plaza.objects.create(
            name="Test Plaza", slug="Test", permissions="{}"
        )

        # Add one membership
        self.membership = Member.objects.create(
            user=self.user_1, plaza=self.plaza, member_type="MB"
        )

        self.post = Post.objects.create(
            title="Test Post",
            content="Test Content",
            plaza=self.plaza,
            user=self.user_1,
            profile=self.profile_1,
            permissions="{}",
            reactions="{}",
        )

        self.client = APIClient()

    def test_get_activity(self):
        """Test we get a HTTP 200 response when looking at list view."""
        self.client.force_authenticate(self.user_1)

        # Get some data
        response = self.client.get("/v1/users/{}/activity/".format(self.user_1.id))

        factory = APIRequestFactory()
        request = factory.get("/v1/users/{}/activity/".format(self.user_1.id))

        force_authenticate(request, user=self.user_1)

        serializer_context = {
            "request": Request(request),
        }

        serializer = PostSerializer(instance=self.post, context=serializer_context)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0], serializer.data)

    def test_get_activity_unauth(self):
        """Test we get a HTTP 404 response when looking at list view."""

        # Get some data
        response = self.client.get("/v1/users/{}/activity/".format(self.user_1.id))

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_activity(self):
        """Test we get a HTTP 404 response when attempting to delete data."""
        self.client.force_authenticate(self.user_1)

        # Set the delete type
        response = self.client.delete(
            "/v1/users/{}/activity/{}/".format(self.user_1.id, self.membership.id)
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_activity_unauth(self):
        """Test we get a HTTP 404 response when attempting to delete data and we aren't authorised."""

        # Set the delete type
        response = self.client.delete(
            "/v1/users/{}/activity/{}/".format(self.user_1.id, self.membership.id)
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_put_activity(self):
        """Test we get a HTTP 404 response when attempting to update data."""
        self.client.force_authenticate(self.user_1)

        # Set the payload
        payload = {"title": "test"}
        response = self.client.put(
            "/v1/users/{}/activity/{}/".format(self.user_1.id, self.membership.id),
            payload,
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_put_activity_unauth(self):
        """Test we get a HTTP 404 response when attempting to update data and we aren't authorised."""
        # Set the payload
        payload = {"title": "test"}
        response = self.client.put(
            "/v1/users/{}/activity/{}/".format(self.user_1.id, self.membership.id),
            payload,
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_post_activity(self):
        """Test we get a HTTP 405 response when attempting to add data."""
        self.client.force_authenticate(self.user_1)

        # Set the payload
        payload = {
            "title": "test post with HTTP",
            "content": "content",
            "user": self.user_1.id,
            "profile": self.profile_1.id,
            "reactions": "{}",
            "permissions": "{}",
            "tags": list(),
        }

        response = self.client.post(
            "/v1/users/{}/activity/".format(self.user_1.id), payload
        )

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_post_activity_unauth(self):
        """Test we get a HTTP 401 response when attempting to add data as we aren't authorised."""

        # Set the payload
        payload = {
            "title": "test post with HTTP",
            "content": "content",
            "user": self.user_1.id,
            "profile": self.profile_1.id,
            "reactions": "{}",
            "permissions": "{}",
            "tags": list(),
        }

        response = self.client.post(
            "/v1/users/{}/activity/".format(self.user_1.id), payload
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
