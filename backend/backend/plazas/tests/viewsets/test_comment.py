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

from ...models import Plaza, Post, Comment
from accounts.models import Profile
from ...serializers import CommentSerializer


class CommentViewsetTest(APITestCase):
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

        self.user_2 = User.objects.create(
            username="user_2",
            first_name="Test",
            last_name="User2",
            email="admin@test2.com",
            is_staff=False,
        )

        self.profile_2 = Profile.objects.create(
            user=self.user_2,
            display_name="tester2",
            global_anonymous=False,
        )

        self.plaza = Plaza.objects.create(
            name="Test Plaza", slug="Test", permissions="{}"
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

        self.comment = Comment.objects.create(
            post=self.post,
            profile=self.profile_1,
            user=self.user_1,
            content="Test Comment",
            reactions="{}",
        )

        self.post2 = Post.objects.create(
            title="Test Post 2",
            content="Test Content",
            plaza=self.plaza,
            user=self.user_1,
            profile=self.profile_1,
            permissions="{}",
            reactions="{}",
        )

        self.comment2 = Comment.objects.create(
            post=self.post2,
            profile=self.profile_1,
            user=self.user_1,
            content="Test Comment 2",
            reactions="{}",
        )

        self.client = APIClient()

    def test_get_comments(self):
        """Test we get a HTTP 200 response when looking at list view."""

        # Now test the actual data is the same
        self.client.force_authenticate(self.user_1)
        response = self.client.get(
            "/v1/plazas/{}/posts/{}/comments/".format(self.plaza.slug, self.plaza.id)
        )

        factory = APIRequestFactory()
        request = factory.get(
            "/v1/plazas/{}/posts/{}/comments/".format(self.plaza.slug, self.plaza.id)
        )

        serializer_context = {
            "request": Request(request),
        }

        serializer = CommentSerializer(
            instance=self.comment, context=serializer_context
        )

        # Check with the data direct from model
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)
        self.assertEqual(response.data["results"][0], serializer.data)

    def test_get_comments_unauth(self):
        """Test we get a HTTP 401 response when looking at list view."""

        # Get some data
        response = self.client.get(
            "/v1/plazas/{}/posts/{}/".format(self.plaza.slug, self.plaza.id)
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_comment_unauth(self):
        """Test we get a HTTP 401 response when looking at detailed view."""

        # Get some data
        response = self.client.get(
            "/v1/plazas/{}/posts/{}/".format(self.plaza.slug, self.post.id)
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_comment(self):
        """Test we get a HTTP 200 response when looking at detailed view."""

        # Get some data
        self.client.force_authenticate(self.user_1)
        # Get some data
        response = self.client.get(
            "/v1/plazas/{}/posts/{}/comments/{}/".format(
                self.plaza.slug, self.post.id, self.comment.id
            )
        )

        factory = APIRequestFactory()
        request = factory.get(
            "/v1/plazas/{}/posts/{}/comments/{}/".format(
                self.plaza.slug, self.plaza.id, self.comment.id
            )
        )

        serializer_context = {
            "request": Request(request),
        }

        serializer = CommentSerializer(
            instance=self.comment, context=serializer_context
        )

        # Check with the data direct from model
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_delete_comment(self):
        """Test we get a HTTP 405 response when attempting to delete data."""
        self.client.force_authenticate(self.user_1)

        # Set the delete type
        response = self.client.delete(
            "/v1/plazas/{}/posts/{}/comments/{}/".format(
                self.plaza.slug, self.post.id, self.comment.id
            )
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_comment_unauth(self):
        """Test we get a HTTP 401 response when attempting to delete data and we aren't authorised."""

        # Set the delete type
        response = self.client.delete(
            "/v1/plazas/{}/posts/{}/comments/{}/".format(
                self.plaza.slug, self.post.id, self.comment.id
            )
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_put_comment(self):
        """Test we get a HTTP 405 response when attempting to update data."""
        self.client.force_authenticate(self.user_1)

        # Set the payload
        payload = {"content": "test2"}
        response = self.client.put(
            "/v1/plazas/{}/posts/{}/comments/{}/".format(
                self.plaza.slug, self.post.id, self.comment.id
            ),
            payload,
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_put_comment_unauth(self):
        """Test we get a HTTP 401 response when attempting to update data and we aren't authorised."""
        # Set the payload
        payload = {"content": "test2"}
        response = self.client.put(
            "/v1/plazas/{}/posts/{}/comments/{}/".format(
                self.plaza.slug, self.post.id, self.comment.id
            ),
            payload,
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_post_comment(self):
        """Test we get a HTTP 201 response when attempting to add data."""
        self.client.force_authenticate(self.user_1)

        # Set the payload
        payload = {
            "content": "testing content with HTTP",
            "user": self.user_1.id,
            "profile": self.profile_1.id,
            "reactions": "{}",
        }

        response = self.client.post(
            "/v1/plazas/{}/posts/{}/comments/".format(self.plaza.slug, self.post.id),
            json.dumps(payload),
            content_type="application/json",
        )

        exists = Comment.objects.filter(
            content="testing content with HTTP",
            profile=self.profile_1.id,
        ).exists()

        self.assertTrue(exists)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_comment_unverified(self):
        """Test we get a HTTP 403 response when attempting to add data as we aren't verified."""
        self.client.force_authenticate(self.user_2)

        # Set the payload
        payload = {
            "content": "testing content with HTTP",
            "user": self.user_1.id,
            "profile": self.profile_1.id,
            "reactions": "{}",
        }

        response = self.client.post(
            "/v1/plazas/{}/posts/{}/comments/".format(self.plaza.slug, self.comment.id),
            json.dumps(payload),
            content_type="application/json",
        )

        exists = Post.objects.filter(
            title="testing content with HTTP",
            profile=self.profile_2.id,
        ).exists()

        self.assertFalse(exists)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_comment_with_unauth(self):
        """Test we get a HTTP 401 response when attempting to add data as we are not authorised."""

        # Set the payload
        payload = {
            "content": "testing content with HTTP",
            "user": self.user_2.id,
            "profile": self.profile_2.id,
            "reactions": "{}",
        }
        response = self.client.post(
            "/v1/plazas/{}/posts/{}/comments/".format(self.plaza.slug, self.comment.id),
            payload,
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_comment_count(self):
        """Test we get the correct comment count when looking at the Plaza view."""

        # Now test the actual data is the same
        self.client.force_authenticate(self.user_1)
        response = self.client.get(
            "/v1/plazas/{}/posts/{}/".format(self.plaza.slug, self.post.id)
        )

        # Check with the data direct from model
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["replies"], 1)
