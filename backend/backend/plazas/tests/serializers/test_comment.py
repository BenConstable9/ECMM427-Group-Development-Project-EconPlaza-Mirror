from rest_framework.test import APIRequestFactory, APITestCase
from rest_framework.request import Request
from django.contrib.auth import get_user_model

from ...serializers import CommentSerializer
from ...models import Plaza, Post, Comment

from accounts.models import Profile


class CommentSerializerTest(APITestCase):
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

        self.comment = Comment.objects.create(
            post=self.post,
            profile=self.profile_1,
            user=self.user_1,
            content="Test Comment",
            reactions="{}",
        )

        # Add the request context
        factory = APIRequestFactory()
        request = factory.get(
            "/plaza/{}/posts/{}/comments".format(plaza.slug, self.post.id)
        )

        serializer_context = {
            "request": Request(request),
        }

        # Serialise the data
        self.serializer = CommentSerializer(
            instance=self.comment, context=serializer_context
        )

    def test_contains_expected_fields(self):
        """Test the serialiser returns the expected fields."""

        data = self.serializer.data

        self.assertEqual(
            set(data.keys()),
            set(
                [
                    "id",
                    "profile",
                    "content",
                    "parent",
                    "children",
                    "reactions",
                    "hidden",
                    "deleted",
                    "created_at",
                ]
            ),
        )

        # Check we aren't exposing fields we don't want to
        self.assertNotIn("user", data.keys())

    def test_equal_data(self):
        """Test the serialiser returns the expected values."""

        data = self.serializer.data

        self.assertEqual(data["id"], self.comment.id)
        self.assertEqual(data["profile"]["id"], self.profile_1.id)
        self.assertEqual(data["content"], self.comment.content)
        self.assertEqual(data["hidden"], self.comment.hidden)
