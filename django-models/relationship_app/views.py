from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book, Library  # Import the Book and Library models

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()  # Query all books from the database
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view to display details for a specific library
class LibraryDetailView(DetailView):
    model = Library  # Specify the model to use for this view
    template_name = 'relationship_app/library_detail.html'  # Path to the template

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # You can add additional context if needed
        return context
