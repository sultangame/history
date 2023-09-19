from rest_framework.viewsets import ReadOnlyModelViewSet
from ..api.serializers import PostSerializer
from ..models import Post
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import RetrieveAPIView


class PostViewSet(ReadOnlyModelViewSet):
    queryset = Post.published.all()
    serializer_class = PostSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'category']
    ordering_fields = ['publish', 'category']


class PostDetail(RetrieveAPIView):
    queryset = Post.published.all()
    serializer_class = PostSerializer