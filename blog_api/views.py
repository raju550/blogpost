from rest_framework import generics, permissions
from blog.models import Post, Category
from .serializers import PostSerializer
from rest_framework import filters
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated, BasePermission, IsAdminUser, DjangoModelPermissions, \
    SAFE_METHODS, AllowAny
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import filters
from django.views.generic import ListView
from django_filters.rest_framework import DjangoFilterBackend


class PagListView(LimitOffsetPagination):
    default_limit = 6
    limit_query_param = 'mylimit'
    offset_query_param = 'myoffset'
    max_limit = 9


class PostUserWritePermission(BasePermission):
    massage = "Editing post is restricted to author only"

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user


class PostList(generics.ListAPIView):
    pagination_class = PagListView
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(author=user)


class PostDetail(generics.RetrieveAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        slug = self.request.query_params.get('slug', None)
        print(slug)
        return Post.objects.filter(slug=slug)


class PostListDetailfilter(generics.ListAPIView):
    pagination_class = PagListView
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['$slug', '$content']


class CatListView(generics.ListAPIView):
    pagination_class = PagListView
    permission_classes = [AllowAny]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filter_fields = ['category']
    search_fields = ['id']


class CreatePost(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class AdminPostDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class EditPost(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class DeletePost(generics.RetrieveDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
