# Delete Operation

**Command:**

```python
from bookshelf.models import Book

# Retrieve the book instance to be deleted
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book instance
book.delete()

# Confirm deletion by trying to retrieve all books
books = Book.objects.all()
print(books)
