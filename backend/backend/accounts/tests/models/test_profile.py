from django.contrib.auth import get_user_model
from django.test import TestCase

from ...models import Profile


class ProfileCreationTest(TestCase):
    def setUp(self):
        """Initialise user instance, which creates a profile instance."""
        User = get_user_model()
        self.user = User.objects.create(username="user1")
        self.profile = self.user.profile

    def test_profile_has_user(self):
        """User and profile correctly reference each other."""
        self.assertEqual(self.user, self.profile.user)

    def test_profile_has_str(self):
        """Profile has a defined __str__ method."""
        self.assertEqual(self.profile.__str__(), "user1")
