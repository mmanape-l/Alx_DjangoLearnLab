from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author using the direct filter
author_name = "Author Name"  # replace with an actual author name
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)
print(f"Books by {author_name}:")
for book in books_by_author:
    print(book.title)

# Alternatively, using the reverse relationship from the Author model
# Uncomment the following lines if you want to use the reverse relationship instead
# books_by_author = author.books.all()
# print(f"Books by {author_name}:")
# for book in books_by_author:
#     print(book.title)

# List all books in a library
library_name = "Library Name"  # replace with an actual library name
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()
print(f"Books in {library_name}:")
for book in books_in_library:
    print(book.title)

# Retrieve the librarian for a library
librarian_for_library = library.librarian
print(f"Librarian for {library_name}: {librarian_for_library.name}")
