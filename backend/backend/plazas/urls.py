from django.urls import path

from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

from .viewsets import PlazaViewSet, PostViewSet, CommentViewSet, MemberViewSet

urlpatterns = []

router = DefaultRouter()

router.register(r"", PlazaViewSet)

post_router = routers.NestedSimpleRouter(router, r"", lookup="plazas")
post_router.register(r"posts", PostViewSet, basename="plaza-post")

comment_router = routers.NestedSimpleRouter(post_router, r"posts", lookup="posts")
comment_router.register(r"comments", CommentViewSet, basename="plaza-post-comment")

member_router = routers.NestedSimpleRouter(router, r"", lookup="plazas")
member_router.register(r"membership", MemberViewSet, basename="plaza-membership")

urlpatterns += router.urls
urlpatterns += post_router.urls
urlpatterns += comment_router.urls
urlpatterns += member_router.urls
