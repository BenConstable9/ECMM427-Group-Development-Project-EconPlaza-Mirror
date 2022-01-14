from rest_framework.routers import DefaultRouter

from .viewsets import PlazaViewSet

urlpatterns = []

router = DefaultRouter()

router.register(r"", PlazaViewSet)

urlpatterns += router.urls
