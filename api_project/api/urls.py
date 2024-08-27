from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, BookList
from django.urls import path, include

# Create a router and register the BookViewSet with it
router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    # URL pattern for the old BookList view (optional)
    path('books/', BookList.as_view(), name='book-list'),
    
    # Include the router-generated URLs
    path('', include(router.urls)),
]
