from django.contrib.auth import get_user_model
from django.test import TestCase

from accounts.models import Profile
from ...models import Plaza, AvailableTag, Tag


class TagCreationTest(TestCase):
    def setUp(self):
        """Initialise post model instance."""

        plaza = Plaza.objects.create(name="Test Plaza", slug="Test", permissions="{}")

        available_tag = AvailableTag.objects.create(name="Test Tag")

        self.tag = Tag.objects.create(
            tag=available_tag,
            content_object=plaza,
        )

    def test_tag_has_str(self):
        """Comment has a defined __str__ method."""
        self.assertEqual(self.tag.__str__(), "Test Tag")
