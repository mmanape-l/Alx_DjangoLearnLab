from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library  # Ensure the Library model is imported

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()  # Retrieve all Book instances from the database
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view to display details for a specific library
class LibraryDetailView(DetailView):
    model = Library  # Use the Library model
    template_name = 'relationship_app/library_detail.html'  # Path to the template

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Additional context can be added if needed
        return context
