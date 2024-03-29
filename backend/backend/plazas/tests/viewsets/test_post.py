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

from ...models import Plaza, Post, Member
from accounts.models import Profile
from ...serializers import PostSerializer


class PostViewsetTest(APITestCase):
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

        Member.objects.create(user=self.user_1, plaza=self.plaza, member_type="MB")

        self.post = Post.objects.create(
            title="Test Post",
            content="Test Content",
            plaza=self.plaza,
            user=self.user_1,
            profile=self.profile_1,
            permissions="{}",
            reactions="{}",
        )

        # Needed to force the serializer to return these fields. Added in the viewset annotations
        self.post.replies = 0
        self.post.last_activity = None

        self.client = APIClient()

    def test_get_posts(self):
        """Test we get a HTTP 200 response when looking at list view."""

        # Now test the actual data is the same
        self.client.force_authenticate(self.user_1)
        response = self.client.get("/v1/plazas/{}/posts/".format(self.plaza.slug))

        factory = APIRequestFactory()
        request = factory.get("/v1/plazas/{}/posts/".format(self.plaza.slug))

        force_authenticate(request, user=self.user_1)

        serializer_context = {
            "request": Request(request),
        }

        serializer = PostSerializer(instance=self.post, context=serializer_context)

        # Check with the data direct from model
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)
        self.assertEqual(response.data["results"][0], serializer.data)

    def test_get_posts_without_plaza(self):
        """Test we get a HTTP 200 response when looking at list view."""

        # Now test the actual data is the same
        self.client.force_authenticate(self.user_1)
        response = self.client.get("/v1/posts/")

        factory = APIRequestFactory()
        request = factory.get("/v1/posts/")
        force_authenticate(request, user=self.user_1)

        serializer_context = {
            "request": Request(request),
        }

        serializer = PostSerializer(instance=self.post, context=serializer_context)

        # Check with the data direct from model
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)
        self.assertEqual(response.data["results"][0], serializer.data)

    def test_get_posts_unauth(self):
        """Test we get a HTTP 401 response when looking at list view."""

        # Get some data
        response = self.client.get("/v1/plazas/{}/posts/".format(self.plaza.slug))

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_posts_unauth_without_plaza(self):
        """Test we get a HTTP 401 response when looking at list view."""

        # Get some data
        response = self.client.get("/v1/posts/")

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)  #

    def test_get_post_without_plaza(self):
        """Test we get a HTTP 403 response when looking at detailed view."""

        # Get some data
        self.client.force_authenticate(self.user_1)
        response = self.client.get("/v1/posts/{}/".format(self.post.id))

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_post_unauth_without_plaza(self):
        """Test we get a HTTP 403 response when looking at detailed view."""

        # Get some data
        response = self.client.get("/v1/posts/{}/".format(self.post.id))

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_post_unauth(self):
        """Test we get a HTTP 401 response when looking at detailed view."""

        # Get some data
        response = self.client.get(
            "/v1/plazas/{}/posts/{}/".format(self.plaza.slug, self.post.id)
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_post(self):
        """Test we get a HTTP 200 response when looking at detailed view."""

        # Get some data
        self.client.force_authenticate(self.user_1)
        response = self.client.get(
            "/v1/plazas/{}/posts/{}/".format(self.plaza.slug, self.post.id)
        )

        factory = APIRequestFactory()
        request = factory.get(
            "/v1/plazas/{}/posts/{}/".format(self.plaza.slug, self.post.id)
        )

        force_authenticate(request, user=self.user_1)

        serializer_context = {
            "request": Request(request),
        }

        serializer = PostSerializer(instance=self.post, context=serializer_context)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_delete_post_without_plaza(self):
        """Test we get a HTTP 405 response when attempting to delete data."""
        self.client.force_authenticate(self.user_1)

        # Set the delete type
        response = self.client.delete("/v1/posts/{}/".format(self.post.id))

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_post(self):
        """Test we get a HTTP 405 response when attempting to delete data."""
        self.client.force_authenticate(self.user_1)

        # Set the delete type
        response = self.client.delete(
            "/v1/plazas/{}/posts/{}/".format(self.plaza.slug, self.post.id)
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_post_unauth(self):
        """Test we get a HTTP 401 response when attempting to delete data and we aren't authorised."""

        # Set the delete type
        response = self.client.delete(
            "/v1/plazas/{}/posts/{}/".format(self.plaza.slug, self.post.id)
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_put_post(self):
        """Test we get a HTTP 405 response when attempting to update data."""
        self.client.force_authenticate(self.user_1)

        # Set the payload
        payload = {"title": "test2"}
        response = self.client.put(
            "/v1/plazas/{}/posts/{}/".format(self.plaza.slug, self.post.id), payload
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_put_post_without_plaza(self):
        """Test we get a HTTP 401 response when attempting to update data and we aren't authorised."""
        # Set the payload
        payload = {"title": "test2"}
        response = self.client.put("/v1/posts/{}/".format(self.post.id), payload)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_put_post_unauth(self):
        """Test we get a HTTP 401 response when attempting to update data and we aren't authorised."""
        # Set the payload
        payload = {"title": "test2"}
        response = self.client.put(
            "/v1/plazas/{}/posts/{}/".format(self.plaza.slug, self.post.id), payload
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_post_post(self):
        """Test we get a HTTP 201 response when attempting to add data."""
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
            "/v1/plazas/{}/posts/".format(self.plaza.slug),
            json.dumps(payload),
            content_type="application/json",
        )

        exists = Post.objects.filter(
            title="test post with HTTP",
            profile=self.profile_1.id,
        ).exists()

        self.assertTrue(exists)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_post_unverified(self):
        """Test we get a HTTP 403 response when attempting to add data as we aren't verified."""
        self.client.force_authenticate(self.user_2)

        # Set the payload
        payload = {
            "title": "test post with HTTP",
            "content": "content",
            "user": self.user_2.id,
            "profile": self.profile_2.id,
            "reactions": "{}",
            "permissions": "{}",
        }

        response = self.client.post(
            "/v1/plazas/{}/posts/".format(self.plaza.slug),
            json.dumps(payload),
            content_type="application/json",
        )

        exists = Post.objects.filter(
            title="test post with HTTP",
            profile=self.profile_2.id,
        ).exists()

        self.assertFalse(exists)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_post_without_plaza(self):
        """Test we get a HTTP 403 response when attempting to add data as we aren't verified."""
        self.client.force_authenticate(self.user_1)

        # Set the payload
        payload = {
            "title": "test post with HTTP",
            "content": "content",
            "user": self.user_1.id,
            "profile": self.profile_1.id,
            "reactions": "{}",
            "permissions": "{}",
        }

        response = self.client.post(
            "/v1/posts/",
            json.dumps(payload),
            content_type="application/json",
        )

        exists = Post.objects.filter(
            title="test post with HTTP",
            profile=self.profile_2.id,
        ).exists()

        self.assertFalse(exists)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_post_with_unauth(self):
        """Test we get a HTTP 401 response when attempting to add data as we are not authorised."""

        # Set the payload
        payload = {
            "title": "test post with HTTP",
            "content": "content",
            "user": self.user_2.id,
            "profile": self.profile_2.id,
            "reactions": "{}",
            "permissions": "{}",
        }
        response = self.client.post(
            "/v1/plazas/{}/posts/".format(self.plaza.slug), payload
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_invalid_post(self):
        """Test we get a HTTP 404 response when looking at the detailed view."""

        # Make an authenticated request to the view...
        self.client.force_authenticate(self.user_1)
        response = self.client.get(
            "/v1/plazas/{}/posts/{}/".format(self.plaza.slug, 200)
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_post_view(self):
        """Test the post view count increases"""

        # Make an authenticated request to the view...
        self.client.force_authenticate(self.user_1)
        response = self.client.post(
            "/v1/plazas/{}/posts/{}/view/".format(self.plaza.slug, self.post.id)
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        post = Post.objects.get(id=self.post.id)

        self.assertEqual(post.views, 1)

    def test_post_view_no_spam(self):
        """Test the post view count doesn't increase multiple times for the same ip"""

        # Make an authenticated request to the view...
        self.client.force_authenticate(self.user_1)
        response = self.client.post(
            "/v1/plazas/{}/posts/{}/view/".format(self.plaza.slug, self.post.id)
        )
        response = self.client.post(
            "/v1/plazas/{}/posts/{}/view/".format(self.plaza.slug, self.post.id)
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        post = Post.objects.get(id=self.post.id)

        self.assertEqual(post.views, 1)
