from django.urls import path
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from .views import list_books
from .views import LibraryDetailView
from .views import register

urlpatterns = [
    # Function-based view for listing books
    path('books/', list_books, name='list_books'),
    
    # Class-based view for library details
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    
    # Authentication views
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', register, name='register'),  # Custom view for user registration
]




