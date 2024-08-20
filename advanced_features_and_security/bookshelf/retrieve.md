# Retrieve Operation

**Command:**

```python
from bookshelf.models import Book

# Retrieve the book instance with the title "1984"
book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)

