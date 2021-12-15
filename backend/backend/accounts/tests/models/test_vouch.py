from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from django.db import IntegrityError
from django.test import TestCase

from ...models import Vouch, User

class VouchCreationTest(TestCase):
    def setUp(self):
        """Initialise user instance, which creates a profile instance."""
        
        self.user_1 = User.objects.create(username="user_1")

        self.user_2 = User.objects.create(username="user_2")

    def test_string_representation(self):
        """Test vouch has appropriate string method"""

        vouch = Vouch.objects.create(voucher=self.user_2, vouchee=self.user_1)
        self.assertEqual(str(vouch), self.user_2.username)

    def test_no_duplicate_vouch(self):
        """Check that you can only vouch for a single user once"""

        Vouch.objects.create(voucher=self.user_1, vouchee=self.user_2)
        with self.assertRaisesMessage(IntegrityError, "UNIQUE constraint failed: accounts_vouch.voucher_id, accounts_vouch.vouchee_id"):
            Vouch.objects.create(voucher=self.user_1, vouchee=self.user_2)
