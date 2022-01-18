from django.urls import path

from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

from .viewsets import PlazaViewSet, PostViewSet

urlpatterns = []

router = DefaultRouter()

router.register(r"", PlazaViewSet)

post_router = routers.NestedSimpleRouter(router, r"", lookup="plazas")
post_router.register(r"posts", PostViewSet, basename="plaza-post")

urlpatterns += router.urls
urlpatterns += post_router.urls
