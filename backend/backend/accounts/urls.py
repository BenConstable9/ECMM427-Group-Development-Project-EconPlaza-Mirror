from django.contrib import admin
from django.urls import path

from rest_framework.routers import DefaultRouter

from .viewsets import VouchViewSet
from .viewsets import UserViewSet


urlpatterns = []

router = DefaultRouter()

router.register(r"vouches", VouchViewSet)
router.register(r"users", UserViewSet)
urlpatterns += router.urls
