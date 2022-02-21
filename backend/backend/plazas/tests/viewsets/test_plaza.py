from datetime import timedelta

from rest_framework.request import Request
from rest_framework.test import (
    APIRequestFactory,
    APITestCase,
    force_authenticate,
    APIClient,
)
from rest_framework import status
from django.contrib.auth import get_user_model
from django.utils import timezone

from ..factory import create_plaza, create_post, create_comment
from ...models import Member
from accounts.models import Profile
from ...serializers import PlazaSerializer


class PlazaViewsetTest(APITestCase):
    def setUp(self):
        """Initialise user instance, which creates a profile instance."""

        User = get_user_model()

        self.user_1 = User.objects.create(
            username="user_1",
            first_name="Test",
            last_name="User",
            email="admin@test.com",
            is_staff=False,
            verified=True,
        )

        self.profile_1 = Profile.objects.create(
            user=self.user_1,
            display_name="tester",
            global_anonymous=False,
        )

        self.user_2 = User.objects.create(
            username="user_2",
            first_name="Test",
            last_name="User2",
            email="admin@test2.com",
            is_staff=False,
        )

        self.profile_2 = Profile.objects.create(
            user=self.user_2,
            display_name="tester2",
            global_anonymous=False,
        )

        self.plaza = create_plaza()

        self.plaza_2 = create_plaza()

        Member.objects.create(user=self.user_1, plaza=self.plaza, member_type="MB")

        self.post = create_post(
            user=self.user_1, profile=self.profile_1, plaza=self.plaza
        )

        self.client = APIClient()

    def test_get_plazas(self):
        """Test we get the correct list of plazas"""

        # Now test the actual data is the same
        self.client.force_authenticate(self.user_1)
        response = self.client.get("/v1/plazas/")

        factory = APIRequestFactory()
        request = factory.get("/v1/plazas/")

        force_authenticate(request, user=self.user_1)

        serializer_context = {
            "request": Request(request),
        }

        serializer = PlazaSerializer(instance=self.plaza, context=serializer_context)

        # Check with the data direct from model
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 2)
        self.assertEqual(response.data["results"][0], serializer.data)

    def test_get_my_plazas(self):
        """Test we get the plazas user 1 is a member of first"""

        # Now test the actual data is the same
        self.client.force_authenticate(self.user_1)
        response = self.client.get("/v1/plazas/?my")

        # Check with the data direct from model
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["membership"]["member"], True)
        self.assertEqual(response.data[1]["membership"]["member"], False)

    def test_get_my_plazas_is_ordered_by_activity(self):
        """Test that we get plazas ordered by most recent activity"""

        # Add some more plazas

        plaza_3 = create_plaza()
        plaza_4 = create_plaza()

        # Add users to plazas as members

        Member.objects.create(user=self.user_1, plaza=plaza_3, member_type="MB")
        Member.objects.create(user=self.user_2, plaza=plaza_3, member_type="MB")
        Member.objects.create(user=self.user_1, plaza=plaza_4, member_type="MB")

        # Create posts in plazas

        post_1 = create_post(
            user=self.user_1,
            profile=self.profile_1,
            plaza=plaza_4,
            created_at=timezone.now() + timedelta(days=1, hours=1),
        )
        post_2 = create_post(
            user=self.user_2,
            profile=self.profile_2,
            plaza=plaza_3,
            created_at=timezone.now() + timedelta(days=1, hours=2),
        )

        # Create comments on posts

        comment_1 = create_comment(
            user=self.user_1,
            profile=self.profile_1,
            post=post_2,
            created_at=timezone.now() + timedelta(days=1, hours=5),
        )

        # Make request

        self.client.force_authenticate(self.user_1)
        response = self.client.get("/v1/plazas/?my")

        # Check with the data direct from model
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)
        self.assertEqual(response.data[0]["slug"], plaza_3.slug)
        self.assertEqual(response.data[1]["slug"], plaza_4.slug)
        self.assertEqual(response.data[2]["slug"], self.plaza.slug)

    def test_get_popular_plazas(self):
        """Test that we can get popular plazas"""

        # Add some more plazas

        plaza_3 = create_plaza()
        plaza_4 = create_plaza()

        # Add users to plazas as members

        Member.objects.create(user=self.user_1, plaza=plaza_3, member_type="MB")
        Member.objects.create(user=self.user_2, plaza=plaza_3, member_type="MB")
        Member.objects.create(user=self.user_1, plaza=plaza_4, member_type="MB")

        # Create posts in plazas

        # This is the most popular post, but it is now too old and shouldn't appear
        old_popular_post = create_post(
            user=self.user_1,
            profile=self.profile_1,
            plaza=plaza_4,
            created_at=timezone.now() + timedelta(days=-15),
            views=9999,
        )

        aging_post = create_post(
            user=self.user_1,
            profile=self.profile_1,
            plaza=plaza_4,
            created_at=timezone.now() + timedelta(days=-10),
            views=4,
        )

        # This should be the most popular post that isn't too old
        new_popular_post = create_post(
            user=self.user_2,
            profile=self.profile_2,
            plaza=plaza_3,
            created_at=timezone.now() + timedelta(days=-2),
            views=200,
        )

        new_post = create_post(
            user=self.user_2,
            profile=self.profile_2,
            plaza=self.plaza,
            created_at=timezone.now() + timedelta(days=-1),
            views=6,
        )

        new_post = create_post(
            user=self.user_1,
            profile=self.profile_1,
            plaza=self.plaza,
            created_at=timezone.now() + timedelta(days=-3),
            views=2,
        )

        new_post = create_post(
            user=self.user_2,
            profile=self.profile_2,
            plaza=self.plaza_2,
            created_at=timezone.now() + timedelta(hours=-5),
            views=12,
        )

        # Make request

        self.client.force_authenticate(self.user_1)
        response = self.client.get("/v1/plazas/?popular")

        # Check with the data direct from model
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)
        self.assertEqual(response.data[0]["slug"], plaza_3.slug)
        self.assertEqual(response.data[1]["slug"], self.plaza_2.slug)
        self.assertEqual(response.data[2]["slug"], self.plaza.slug)
