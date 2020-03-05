from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    addComment,
    addLike,
    addFollower,
    getFollowers,
    removeFollower,
    search,
    getSubscribed,
    webhook
)

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("user/<str:username>", UserPostListView.as_view(), name="user-posts"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('add-comment/', addComment, name='add-comment'),
    path('add-like/', addLike, name='add-like'),
    path('add-follower/', addFollower, name='add-follower'),
    path('remove-follower/', removeFollower, name='remove-follower'),
    path('get-followers/', getFollowers, name='get-followers'),
    path('get-subscribed/', getSubscribed, name='get-subscribed'),
    path('search/', search, name='search'),
    path('webhook/', webhook, name='webhook'),

]
