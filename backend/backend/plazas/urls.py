from rest_framework_nested import routers

from .viewsets import PlazaViewSet, PostViewSet, CommentViewSet, MemberViewSet

urlpatterns = []

router = routers.SimpleRouter()

router.register(r"plazas", PlazaViewSet, basename="plazas")

router.register(r"posts", PostViewSet, basename="posts")

post_router = routers.NestedSimpleRouter(router, r"plazas", lookup="plazas")
post_router.register(r"posts", PostViewSet, basename="plaza-post")

comment_router = routers.NestedSimpleRouter(post_router, r"posts", lookup="posts")
comment_router.register(r"comments", CommentViewSet, basename="plaza-post-comment")

member_router = routers.NestedSimpleRouter(router, r"plazas", lookup="plazas")
member_router.register(r"membership", MemberViewSet, basename="plaza-membership")

urlpatterns += router.urls
urlpatterns += post_router.urls
urlpatterns += comment_router.urls
urlpatterns += member_router.urls
