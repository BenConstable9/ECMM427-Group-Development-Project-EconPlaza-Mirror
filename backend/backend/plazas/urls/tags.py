from rest_framework_nested import routers

from ..viewsets import AvailableTagViewSet

urlpatterns = []

router = routers.SimpleRouter()

router.register(r"", AvailableTagViewSet, basename="posts")

urlpatterns += router.urls
