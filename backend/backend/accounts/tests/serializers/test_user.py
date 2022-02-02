from rest_framework.test import APIRequestFactory, APITestCase
from rest_framework.request import Request
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

from ...serializers import UserSerializer
from ...serializers.user import UserPostSerializer


class UserSerializerTest(APITestCase):
    def setUp(self):
        """Initalise a user."""

        User = get_user_model()

        self.user_1 = User.objects.create(
            username="user_1",
            first_name="Test",
            last_name="User",
            email="admin@test.com",
            is_staff=False,
        )

        # Add the request context
        factory = APIRequestFactory()
        request = factory.get("/accounts/users")

        serializer_context = {
            "request": Request(request),
        }

        # Serialise the data
        self.serializer = UserSerializer(
            instance=self.user_1, context=serializer_context
        )

    def test_contains_expected_fields(self):
        """Test the serialiser returns the expected fields."""

        data = self.serializer.data

        self.assertEqual(
            set(data.keys()),
            set(
                [
                    "id",
                    "username",
                    "email",
                    "verified",
                    "is_staff",
                    "first_name",
                    "last_name",
                    "date_joined",
                ]
            ),
        )

        # Check we aren't exposing fields we don't want to
        self.assertNotIn("password", data.keys())
        self.assertNotIn("twitter_oauth", data.keys())

    def test_equal_data(self):
        """Test the serialiser returns the expected values."""

        data = self.serializer.data

        self.assertEqual(data["id"], self.user_1.id)
        self.assertEqual(data["first_name"], self.user_1.first_name)
        self.assertEqual(data["last_name"], self.user_1.last_name)
        self.assertEqual(data["username"], self.user_1.username)
        self.assertEqual(data["email"], self.user_1.email)
        self.assertEqual(data["is_staff"], self.user_1.is_staff)


class UserPostSerializerTest(APITestCase):
    def setUp(self):
        """Initalise a user."""

        User = get_user_model()

        self.user_1 = User.objects.create(
            username="user_1",
            first_name="Test",
            last_name="User",
            email="admin@test.com",
            password="Orange@132",
        )

        # Add the request context
        factory = APIRequestFactory()
        request = factory.get("/accounts/users")

        serializer_context = {
            "request": Request(request),
        }

        # Serialise the data
        self.serializer = UserPostSerializer(
            instance=self.user_1, context=serializer_context
        )

    def test_contains_expected_fields(self):
        """Test the serialiser returns the expected fields."""

        data = self.serializer.data

        self.assertEqual(
            set(data.keys()),
            set(
                [
                    "id",
                    "username",
                    "email",
                    "first_name",
                    "last_name",
                ]
            ),
        )

        # Check we aren't exposing fields we don't want to
        self.assertNotIn("password", data.keys())

    def test_equal_data(self):
        """Test the serialiser returns the expected values."""

        data = self.serializer.data

        self.assertEqual(data["id"], self.user_1.id)
        self.assertEqual(data["first_name"], self.user_1.first_name)
        self.assertEqual(data["last_name"], self.user_1.last_name)
        self.assertEqual(data["username"], self.user_1.username)
        self.assertEqual(data["email"], self.user_1.email)
