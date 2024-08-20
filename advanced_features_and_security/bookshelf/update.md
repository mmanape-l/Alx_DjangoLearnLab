# Update Operation

**Command:**

```python
from bookshelf.models import Book

# Retrieve the book instance with the original title
book = Book.objects.get(title="1984")

# Update the title of the book
book.title = "Nineteen Eighty-Four"
book.save()

# Verify the update
updated_book = Book.objects.get(title="Nineteen Eighty-Four")
print(updated_book.title, updated_book.author, updated_book.publication_year)
