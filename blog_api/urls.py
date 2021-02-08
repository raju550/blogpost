from django.urls import path
from .views import PostList, PostDetail, PostListDetailfilter, CatListView, CreatePost, EditPost, AdminPostDetail, \
    DeletePost

app_name = 'blog_api'

urlpatterns = [
    path('posts/<str:pk>/', PostDetail.as_view(), name='detailcreate'),
    path('search/', PostListDetailfilter.as_view(), name='postsearch'),
    path('category/', CatListView.as_view(), name='categorysearch'),
    path('', PostList.as_view(), name='listcreate'),
    path('admin/create/', CreatePost.as_view(), name='createpost'),
    path('admin/edit/postdetail/<int:pk>/', AdminPostDetail.as_view(), name='admindetailpost'),
    path('admin/edit/<int:pk>/', EditPost.as_view(), name='editpost'),
    path('admin/delete/<int:pk>/', DeletePost.as_view(), name='deletepost'),
]
