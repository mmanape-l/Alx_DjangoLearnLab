from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_book, name='add_book'),
    path('edit/<int:pk>/', views.edit_book, name='edit_book'),
    path('delete/<int:pk>/', views.delete_book, name='delete_book'),
    # Ensure you have a URL pattern for listing books, if used in redirect
    path('list/', views.book_list, name='book_list'),  # Example URL pattern for listing books
]
