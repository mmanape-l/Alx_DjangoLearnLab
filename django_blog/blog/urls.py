from django.urls import path
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView, 
    PostUpdateView, 
    PostDeleteView, 
    profile,
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView
)

urlpatterns = [
    # User profile update
    path('profile/', profile, name='profile'),

    # Blog post CRUD operations
    path('', PostListView.as_view(), name='post-list'),  # List all posts
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # View a single post
    path('post/new/', PostCreateView.as_view(), name='post-create'),  # Create a new post
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),  # Edit a post
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),  # Delete a post

    # Comment-related actions
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='add-comment'),  # Add a new comment
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='edit-comment'),  # Edit a comment
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='delete-comment'),  # Delete a comment
]
