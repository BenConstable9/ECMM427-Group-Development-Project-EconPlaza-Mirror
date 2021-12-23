from django.contrib import admin
from django.urls import path

from rest_framework.routers import DefaultRouter

from .viewsets import UserViewSet, VouchViewSet

from .views import AuthenticatedUserView

urlpatterns = [
    path('user/', AuthenticatedUserView.as_view()),
]

router = DefaultRouter()

router.register(r"vouches", VouchViewSet)
router.register(r"users", UserViewSet)

urlpatterns += router.urls
