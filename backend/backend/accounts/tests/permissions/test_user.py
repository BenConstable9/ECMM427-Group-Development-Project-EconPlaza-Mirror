from django.test import RequestFactory, TestCase
from ...permissions import IsAdminOrVerified

from ...models import User

class IsAdminOrVerifiedTest(TestCase):
    def setUp(self):
        """Set up a series of test users"""
        self.admin_user = User.objects.create(username='admin_user', is_staff=True)
        self.non_admin_non_verified_user = User.objects.create(username='non_admin_non_verified_user')

        self.non_admin_verified_user = User.objects.create(username='non_admin_verified_user', verified=1)

        self.factory = RequestFactory()

    def test_admin_user_returns_true(self):
        """Check an admin can override the permission."""

        request = self.factory.delete('/')
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
        
        request = self.factory.delete('/')
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

        request = self.factory.delete('/')
        request.user = self.non_admin_verified_user

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