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
    CommentDeleteView,
    TagListView,
    SearchResultsView,
    PostByTagListView,
    login_view,  # Add this import
    register_view  # Add this import
)

urlpatterns = [
    # User authentication
    path('login/', login_view, name='login'),  # Add this line
    path('register/', register_view, name='register'),  # Add this line

    # User profile update
    path('profile/', profile, name='profile'),

    # Blog post CRUD operations
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/update/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    # Comment-related actions
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='add-comment'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='edit-comment'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='delete-comment'),

    # Tag-related actions
    path('tags/', TagListView.as_view(), name='tag-list'),
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='posts-by-tag'),

    # Search functionality
    path('search/', SearchResultsView.as_view(), name='search-results'),
]