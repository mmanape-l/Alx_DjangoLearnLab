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
        serializer.save()

class BookDetailView(generics.RetrieveAPIView):
    """
    Retrieve a specific book by its ID.
    - GET /books/<int:pk>/ - Retrieve a specific book by its ID.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]  # Allows unauthenticated users to retrieve books

class BookCreateView(generics.CreateAPIView):
    """
    Create a new book.
    - POST /books/ - Create a new book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Restricts access to authenticated users

class BookUpdateView(generics.UpdateAPIView):
    """
    Update an existing book.
    - PUT /books/<int:pk>/ - Update an existing book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Restricts access to authenticated users

class BookDeleteView(generics.DestroyAPIView):
    """
    Delete a book.
    - DELETE /books/<int:pk>/ - Delete a book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Restricts access to authenticated users
