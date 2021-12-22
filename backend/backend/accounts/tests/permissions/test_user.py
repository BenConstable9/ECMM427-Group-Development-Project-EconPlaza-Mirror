from django.contrib.auth import get_user_model
from django.test import RequestFactory, TestCase
from django.contrib.auth import get_user_model
from time import sleep

from ...permissions import IsAdminOrVerified
from ...models import Vouch

class IsAdminOrVerifiedTest(TestCase):
    def setUp(self):
        """Set up a series of test users"""
        User = get_user_model()

        self.admin_user = User.objects.create(username='admin_user', is_staff=True)
        self.non_admin_non_verified_user = User.objects.create(username='non_admin_non_verified_user')

        # This user needs to be vouched for all the signal runs and the user becomes unverified
        self.non_admin_verified_user = User.objects.create(username='non_admin_verified_user')

        # Create three spare users
        user_1 = User.objects.create(username="permission_user_1")
        user_2 = User.objects.create(username="permission_user_2")
        user_3 = User.objects.create(username="permission_user_3")

        # Now add our vouches. This only works as the the restriction on vouching when verified is on the API.
        Vouch.objects.create(voucher=self.admin_user, vouchee=self.non_admin_verified_user)
        Vouch.objects.create(voucher=self.non_admin_non_verified_user, vouchee=self.non_admin_verified_user)
        Vouch.objects.create(voucher=user_1, vouchee=self.non_admin_verified_user)
        Vouch.objects.create(voucher=user_2, vouchee=self.non_admin_verified_user)
        Vouch.objects.create(voucher=user_3, vouchee=self.non_admin_verified_user)

        self.factory = RequestFactory()

    def test_admin_user_returns_true(self):
        """Check an admin can override the permission."""

        request = self.factory.post('/')
        request.user = self.admin_user

        permission_check = IsAdminOrVerified()

        permission = permission_check.has_permission(request, None)

        self.assertTrue(permission)

    def test_admin_user_returns_true_on_safe_method(self):
        """Check we can pass on a safe method."""

        request = self.factory.get('/')
        request.user = self.admin_user

        permission_check = IsAdminOrVerified()

        permission = permission_check.has_permission(request, None)

        self.assertTrue(permission)

    def test_non_admin_non_verified_user_returns_false(self):
        """Test that a non verified and non admin will fail the check."""
        
        request = self.factory.post('/')
        request.user = self.non_admin_non_verified_user

        permission_check = IsAdminOrVerified()

        permission = permission_check.has_permission(request, None)

        self.assertFalse(permission)

    def test_non_admin_non_verified_user_returns_true_on_safe_method(self):
        """Check we can pass on a safe method."""

        request = self.factory.get('/')
        request.user = self.non_admin_non_verified_user

        permission_check = IsAdminOrVerified()

        permission = permission_check.has_permission(request, None)

        self.assertTrue(permission)

    def test_non_admin_verified_user_returns_true(self):
        """Test that a verified user will pass the permissions test."""

        # To get around the signal delay in verification, force verification
        self.non_admin_non_verified_user.verified = True
        self.non_admin_non_verified_user.save()

        request = self.factory.post('/')
        request.user = self.non_admin_non_verified_user

        permission_check = IsAdminOrVerified()

        permission = permission_check.has_permission(request, None)

        self.assertTrue(permission)

    def test_non_admin_verified_user_returns_true_on_safe_method(self):
        """Check we can pass on a safe method."""

        request = self.factory.get('/')
        request.user = self.non_admin_verified_user

        permission_check = IsAdminOrVerified()

        permission = permission_check.has_permission(request, None)

        self.assertTrue(permission)