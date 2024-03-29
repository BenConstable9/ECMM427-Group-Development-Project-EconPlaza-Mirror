from django.contrib import admin
from django.urls import path

from rest_framework.routers import SimpleRouter
from rest_framework_nested import routers

from .viewsets import (
    UserViewSet,
    VouchViewSet,
    ProfileViewSet,
    MembershipViewSet,
    ActivityViewSet,
)

from .views import AuthenticatedUserView

urlpatterns = [
    path("me/", AuthenticatedUserView.as_view()),
]

router = SimpleRouter()

router.register(r"", UserViewSet, basename="users")

profile_router = routers.NestedSimpleRouter(router, r"", lookup="users")
profile_router.register(r"profiles", ProfileViewSet, basename="users-profiles")

memberships_router = routers.NestedSimpleRouter(router, r"", lookup="users")
memberships_router.register(
    r"memberships", MembershipViewSet, basename="users-memberships"
)

activity_router = routers.NestedSimpleRouter(router, r"", lookup="users")
activity_router.register(r"activity", ActivityViewSet, basename="users-activity")

vouch_router = routers.NestedSimpleRouter(router, r"", lookup="users")
vouch_router.register(r"vouches", VouchViewSet, basename="users-vouches")

urlpatterns += router.urls
urlpatterns += profile_router.urls
urlpatterns += memberships_router.urls
urlpatterns += activity_router.urls
urlpatterns += vouch_router.urls
