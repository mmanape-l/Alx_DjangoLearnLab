from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListCreateAPIView):
    """
    List all books or create a new book.
    - GET /books/ - Retrieve a list of all books.
    - POST /books/ - Create a new book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]  # Allows unauthenticated users to list books

    def perform_create(self, serializer):
        """
        Override to add custom behavior when creating a new book.
        """
        # Add custom logic here if needed
        serializer.save()

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a book.
    - GET /books/<int:pk>/ - Retrieve a specific book by its ID.
    - PUT /books/<int:pk>/ - Update an existing book.
    - DELETE /books/<int:pk>/ - Delete a book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Restricts access to authenticated users

    def perform_update(self, serializer):
        """
        Override to add custom behavior when updating a book.
        """
        # Add custom logic here if needed
        serializer.save()

