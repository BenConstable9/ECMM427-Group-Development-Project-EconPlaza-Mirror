from rest_framework_nested import routers

from ..viewsets import PostViewSet

urlpatterns = []

router = routers.SimpleRouter()

router.register(r"", PostViewSet, basename="posts")

urlpatterns += router.urls
