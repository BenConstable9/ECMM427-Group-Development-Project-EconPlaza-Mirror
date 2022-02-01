from rest_framework.test import APIRequestFactory, APITestCase


from ...serializers import AvailableTagSerializer
from ...models import AvailableTag


class AvailableTagSerializerTest(APITestCase):
    def setUp(self):
        """Initalise a post."""

        self.tag = AvailableTag.objects.create(name="Test Tag")

        self.serializer = AvailableTagSerializer(instance=self.tag)

    def test_contains_expected_fields(self):
        """Test the serialiser returns the expected fields."""

        data = self.serializer.data

        self.assertEqual(
            set(data.keys()),
            set(
                [
                    "id",
                    "name",
                    "created_at",
                ]
            ),
        )

    def test_equal_data(self):
        """Test the serialiser returns the expected values."""

        data = self.serializer.data

        self.assertEqual(data["id"], self.tag.id)
        self.assertEqual(data["name"], self.tag.name)
