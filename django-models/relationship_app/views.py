from django.shortcuts import render
from .models import Book, Library  # Import the Book and Library models

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()  # Retrieve all Book instances from the database
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Function-based view to display details for a specific library
def library_detail(request, pk):
    library = get_object_or_404(Library, pk=pk)  # Fetch the library by primary key
    books = library.books.all()  # Retrieve all books associated with this library
    context = {
        'library': library,
        'books': books
    }
    return render(request, 'relationship_app/library_detail.html', context)
