from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from ..serializers import PlazaSerializer, PostSerializer
from ..models import Plaza, Post


class PlazaViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to view Plazas
    """

    queryset = Plaza.objects.all()
    serializer_class = PlazaSerializer
    lookup_field = "slug"

    @action(methods=["GET"], detail=True, url_path="posts")
    def posts(self, request, slug=None):
        posts = Post.objects.all().filter(plaza__slug=slug, hidden=False, deleted=False)
        page = self.paginate_queryset(posts)
        if page is not None:
            serializer = PostSerializer(page, many=True, context={"request": request})
            return self.getPaginatedResponse(serializer.data)
        serializer = PostSerializer(posts, many=True, context={"request": request})
        return Response(serializer.data)
