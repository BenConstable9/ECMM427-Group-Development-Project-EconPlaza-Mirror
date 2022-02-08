from rest_framework.test import APIRequestFactory, APITestCase


from ...serializers import TagSerializer
from ...models import AvailableTag, Plaza, Tag


class TagSerializerTest(APITestCase):
    def setUp(self):
        """Initalise a post."""

        plaza = Plaza.objects.create(name="Test Plaza", slug="Test", permissions="{}")

        self.available_tag = AvailableTag.objects.create(name="Test Tag")

        self.tag = Tag.objects.create(
            tag=self.available_tag,
            content_object=plaza,
        )

        self.serializer = TagSerializer(instance=self.tag)

    def test_contains_expected_fields(self):
        """Test the serialiser returns the expected fields."""

        data = self.serializer.data

        self.assertEqual(
            set(data.keys()),
            set(
                [
                    "id",
                    "tag",
                    "created_at",
                ]
            ),
        )

    def test_equal_data(self):
        """Test the serialiser returns the expected values."""

        data = self.serializer.data

        self.assertEqual(data["id"], self.tag.id)
        self.assertEqual(data["tag"]["name"], self.available_tag.name)
