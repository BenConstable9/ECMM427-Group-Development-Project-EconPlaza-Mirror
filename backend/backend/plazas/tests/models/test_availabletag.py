from django.contrib.auth import get_user_model
from django.test import TestCase

from accounts.models import Profile
from ...models import Plaza, AvailableTag


class AvailableTagCreationTest(TestCase):
    def setUp(self):
        """Initialise post model instance."""
        self.tag = AvailableTag.objects.create(name="Test Tag")

    def test_tag_has_str(self):
        """Comment has a defined __str__ method."""
        self.assertEqual(self.tag.__str__(), "Test Tag")
