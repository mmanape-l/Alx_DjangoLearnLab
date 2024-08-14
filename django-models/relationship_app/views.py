from django.shortcuts import render, get_object_or_404
from .models import Book, Library  # Import the models

# Function-based view to display details for a specific library
def library_detail(request, pk):
    library = get_object_or_404(Library, pk=pk)  # Fetch the library by primary key
    books = library.books.all()  # Get all books associated with this library
    context = {
        'library': library,
        'books': books
    }
    return render(request, 'relationship_app/library_detail.html', context)
