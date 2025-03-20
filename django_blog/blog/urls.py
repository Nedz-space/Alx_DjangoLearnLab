from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import (
    PostListView, PostDetailView,
    PostCreateView, PostUpdateView, PostDeleteView, CommentCreateView, CommentUpdateView, CommentDeleteView, PostByTagListView, search_posts
)
from . import views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),

    # List all posts
    path('', PostListView.as_view(), name='post-list'),

    # Create a new post
    path('post/new/', PostCreateView.as_view(), name='post-create'),

    # View details of a post
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),

    # Update a post
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),

    # Delete a post
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    # Comments URLs
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),

    # Tags and Search
    path('tags/<slug:slug>/', PostByTagListView.as_view(), name='posts-by-tag'),  # ✅ Corrected
    path('search/', search_posts, name='post-search'),
]

