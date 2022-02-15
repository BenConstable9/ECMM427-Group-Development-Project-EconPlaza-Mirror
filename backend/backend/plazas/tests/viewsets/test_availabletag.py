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

from ...models import AvailableTag
from ...serializers import AvailableTagSerializer


class AvailableTagViewsetTest(APITestCase):
    def setUp(self):
        """Initialise user instance, which creates a profile instance."""

        self.availabletag = AvailableTag.objects.create(name="test")

        User = get_user_model()

        self.user_1 = User.objects.create(
            username="user_1",
            first_name="Test",
            last_name="User",
            email="admin@test.com",
            is_staff=False,
            verified=True,
        )

        self.client = APIClient()

    def test_get_tags(self):
        """Test we get a HTTP 200 response when looking at list view."""
        self.client.force_authenticate(self.user_1)

        response = self.client.get("/v1/tags/")

        factory = APIRequestFactory()
        request = factory.get("/v1/tags/")

        serializer_context = {
            "request": Request(request),
        }

        serializer = AvailableTagSerializer(
            instance=self.availabletag, context=serializer_context
        )

        # Check with the data direct from model
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)
        self.assertEqual(response.data["results"][0], serializer.data)

    def test_get_tag(self):
        """Test we get a HTTP 200 response when looking at detailed view."""
        self.client.force_authenticate(self.user_1)

        response = self.client.get("/v1/tags/{}/".format(self.availabletag.name))

        factory = APIRequestFactory()
        request = factory.get("/v1/tags/")

        serializer_context = {
            "request": Request(request),
        }

        serializer = AvailableTagSerializer(
            instance=self.availabletag, context=serializer_context
        )

        # Check with the data direct from model
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_tags_unauth(self):
        """Test we get a HTTP 404 response when looking at list view."""

        # Get some data
        response = self.client.get("/v1/tags/")

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_tag_unauth(self):
        """Test we get a HTTP 404 response when looking at detailed view."""

        # Get some data
        response = self.client.get("/v1/tags/{}/".format(self.availabletag.name))

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_tag(self):
        """Test we get a HTTP 404 response when attempting to delete data."""
        self.client.force_authenticate(self.user_1)

        # Set the delete type
        response = self.client.delete("/v1/tag/{}/".format(self.availabletag.name))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_tag_unauth(self):
        """Test we get a HTTP 404 response when attempting to delete data and we aren't authorised."""

        # Set the delete type
        response = self.client.delete("/v1/tag/{}/".format(self.availabletag.name))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_put_tag(self):
        """Test we get a HTTP 405 response when attempting to update data."""
        self.client.force_authenticate(self.user_1)

        # Set the payload
        payload = {"name": "test2"}
        response = self.client.put(
            "/v1/tags/{}/".format(self.availabletag.name),
            payload,
        )

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_put_tag_unauth(self):
        """Test we get a HTTP 401 response when attempting to update data and we aren't authorised."""
        # Set the payload
        payload = {"name": "test2"}
        response = self.client.put(
            "/v1/tags/{}/".format(self.availabletag.name),
            payload,
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_post_tag(self):
        """Test we get a HTTP 201 response when attempting to add data."""
        self.client.force_authenticate(self.user_1)

        # Set the payload
        payload = {
            "name": "economics",
        }

        response = self.client.post("/v1/tags/", payload)

        exists = AvailableTag.objects.filter(
            name="economics",
        ).exists()

        self.assertTrue(exists)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_member_unauth(self):
        """Test we get a HTTP 403 response when attempting to add data as we aren't authorised."""

        # Set the payload
        payload = {
            "name": "economics-exeter",
        }

        response = self.client.post("/v1/tags/", payload)

        exists = AvailableTag.objects.filter(
            name="economics",
        ).exists()

        self.assertFalse(exists)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_post_tag_spaces(self):
        """Test we get a HTTP 400 response when attempting to add data as tags cannot have spaces."""
        self.client.force_authenticate(self.user_1)

        # Set the payload
        payload = {
            "name": "test with spaces",
        }

        response = self.client.post("/v1/tags/", payload)

        exists = AvailableTag.objects.filter(
            name="test with spaces",
        ).exists()

        self.assertFalse(exists)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
