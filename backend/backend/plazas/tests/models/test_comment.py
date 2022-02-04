from django.contrib.auth import get_user_model
from django.test import TestCase

from accounts.models import Profile
from ...models import Plaza, Post, Comment


class CommentCreationTest(TestCase):
    def setUp(self):
        """Initialise post model instance."""
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

        post = Post.objects.create(
            title="Test Post",
            content="Test Content",
            plaza=plaza,
            user=self.user_1,
            profile=self.profile_1,
            permissions="{}",
            reactions="{}",
        )

        self.comment = Comment.objects.create(
            post=post,
            profile=self.profile_1,
            user=self.user_1,
            content="Test Comment",
            reactions="{}",
        )

    def test_comment_has_str(self):
        """Comment has a defined __str__ method."""
        self.assertEqual(self.comment.__str__(), "Test Comment")
