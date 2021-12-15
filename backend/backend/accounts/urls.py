from django.contrib import admin
from django.urls import path

from rest_framework.routers import DefaultRouter

from .viewsets import VouchViewSet


urlpatterns = []

router = DefaultRouter()
router.register(r"vouches", VouchViewSet)
urlpatterns += router.urls
