import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'libraryproject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        return books
    except Author.DoesNotExist:
        return []

def get_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        return books
    except Library.DoesNotExist:
        return []

def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        return librarian
    except Library.DoesNotExist:
        return None
    except Librarian.DoesNotExist:
        return None

if __name__ == "__main__":
    author_name = "J.K. Rowling"
    print("Books by author:", list(get_books_by_author(author_name)))

    library_name = "Central Library"
    print("Books in library:", list(get_books_in_library(library_name)))
    print("Librarian for library:", get_librarian_for_library(library_name))

