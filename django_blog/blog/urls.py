from django.urls import path
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView, 
    PostUpdateView, 
    PostDeleteView, 
    profile,
    create_comment,
    update_comment,
    delete_comment
)

urlpatterns = [
    # User profile update
    path('profile/', profile, name='profile'),

    # Blog post CRUD operations
    path('', PostListView.as_view(), name='post-list'),  # List all posts
    path('post/<int:pk>/update/', PostDetailView.as_view(), name='post-detail'),  # View a single post
    path('post/new/', PostCreateView.as_view(), name='post-create'),  # Create a new post
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),  # Edit a post
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),  # Delete a post

    # Comment-related actions
    path('post/<int:post_id>/comments/new/', create_comment, name='add-comment'),  # Add a new comment
    path('post/<int:post_id>/comments/<int:comment_id>/edit/', update_comment, name='edit-comment'),  # Edit a comment
    path('post/<int:post_id>/comments/<int:comment_id>/delete/', delete_comment, name='delete-comment'),  # Delete a comment
]
