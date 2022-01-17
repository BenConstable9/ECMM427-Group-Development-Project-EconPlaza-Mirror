from django.contrib.auth import get_user_model
from rest_framework.test import APIRequestFactory, APITestCase
from rest_framework.request import Request
from ...models import Vouch

from ...serializers import VouchSerializer


class VouchSerializerTest(APITestCase):
    def setUp(self):
        """Initalise a series of users and a vouching."""

        User = get_user_model()

        self.user_1 = User.objects.create(username="user_1")

        self.user_2 = User.objects.create(username="user_2")

        self.vouch = Vouch.objects.create(voucher=self.user_1, vouchee=self.user_2)

        factory = APIRequestFactory()
        request = factory.get("/v1/accounts/vouches/{}/".format(self.user_2.id))

        serializer_context = {
            "request": Request(request),
        }

        # Serialise the data
        self.serializer = VouchSerializer(
            instance=self.vouch, context=serializer_context
        )

    def test_contains_expected_fields(self):
        """Test the serialiser returns the expected fields."""

        data = self.serializer.data

        self.assertEqual(set(data.keys()), set(["vouchee", "voucher"]))

    def test_equal_data(self):
        """Test the serialiser returns the expected values."""

        data = self.serializer.data

        self.assertEqual(data["vouchee"], self.user_2.id)
        self.assertEqual(data["voucher"]["id"], self.user_1.id)
