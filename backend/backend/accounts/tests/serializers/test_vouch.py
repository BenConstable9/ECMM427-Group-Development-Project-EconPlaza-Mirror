from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from ...models import Vouch

from ...serializers import VouchSerializer


class VouchSerializerTest(APITestCase):
    def setUp(self):
        """Initalise a series of users and a vouching."""

        User = get_user_model()

        self.user_1 = User.objects.create(username="user_1")

        self.user_2 = User.objects.create(username="user_2")

        self.vouch = Vouch.objects.create(
            voucher=self.user_1, vouchee=self.user_2)

        # Serialise the data
        self.serializer = VouchSerializer(instance=self.vouch)

    def test_contains_expected_fields(self):
        """Test the serialiser returns the expected fields."""

        data = self.serializer.data

        self.assertEqual(set(data.keys()), set(['vouchee', 'voucher']))

    def test_equal_data(self):
        """Test the serialiser returns the expected values."""

        data = self.serializer.data

        self.assertEqual(data['vouchee'], self.user_2.id)
        self.assertEqual(data['voucher'], self.user_1.id)
