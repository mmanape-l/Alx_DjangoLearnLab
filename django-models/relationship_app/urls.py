from django.urls import path
from .views import list_books, LibraryDetailView, user_login, user_logout, register

urlpatterns = [
    # Function-based view for listing books
    path('books/', list_books, name='list_books'),
    
    # Class-based view for library details
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    
    # Authentication views
    path('login/', user_login, name='login'),  # User login
    path('logout/', user_logout, name='logout'),  # User logout
    path('register/', register, name='register'),  # User registration
]

