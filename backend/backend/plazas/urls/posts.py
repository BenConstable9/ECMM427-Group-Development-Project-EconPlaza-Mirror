from rest_framework_nested import routers

from ..viewsets import PlazaViewSet, PostViewSet, CommentViewSet, MemberViewSet

urlpatterns = []

router = routers.SimpleRouter()

router.register(r"", PostViewSet, basename="posts")

urlpatterns += router.urls
