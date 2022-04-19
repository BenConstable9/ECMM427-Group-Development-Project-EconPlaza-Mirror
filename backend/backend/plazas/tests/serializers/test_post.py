from rest_framework.test import APIRequestFactory, APITestCase
from rest_framework.request import Request
from django.contrib.auth import get_user_model

from ...serializers import PostSerializer
from ...models import Plaza, Post

from accounts.models import Profile, profile


class PostSerializerTest(APITestCase):
    def setUp(self):
        """Initalise a post."""

        User = get_user_model()

        self.user_1 = User.objects.create(
            username="user_1",
            first_name="Test",
            last_name="User",
            email="admin@test.com",
            is_staff=False,
        )

        self.profile_1 = Profile.objects.create(
            user=self.user_1,
            display_name="tester",
            global_anonymous=False,
        )

        plaza = Plaza.objects.create(name="Test Plaza", slug="Test", permissions="{}")

        self.post = Post.objects.create(
            title="Test Post",
            content="Test Content",
            plaza=plaza,
            user=self.user_1,
            profile=self.profile_1,
            permissions="{}",
            reactions="{}",
        )

        # Add the request context
        factory = APIRequestFactory()
        request = factory.get("/plaza/{}/posts/{}".format(plaza.slug, self.post.id))

        serializer_context = {
            "request": Request(request),
        }

        # Serialise the data
        self.serializer = PostSerializer(instance=self.post, context=serializer_context)

    def test_contains_expected_fields(self):
        """Test the serialiser returns the expected fields."""

        data = self.serializer.data

        self.assertEqual(
            set(data.keys()),
            set(
                [
                    "id",
                    "profile",
                    "plaza",
                    "title",
                    "content",
                    "permissions",
                    "reactions",
                    "hidden",
                    "views",
                    "created_at",
                    "tags",
                ]
            ),
        )

        # Check we aren't exposing fields we don't want to
        self.assertNotIn("user", data.keys())

    def test_equal_data(self):
        """Test the serialiser returns the expected values."""

        data = self.serializer.data

        self.assertEqual(data["id"], self.post.id)
        self.assertEqual(data["profile"]["id"], self.profile_1.id)
        self.assertEqual(data["title"], self.post.title)
        self.assertEqual(data["content"], self.post.content)
        self.assertEqual(data["hidden"], self.post.hidden)
        self.assertEqual(data["views"], self.post.views)
