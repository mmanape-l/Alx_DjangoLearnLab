# Create Operation

**Command:**

```python
from bookshelf.models import Book

# Create a new book instance using objects.create()
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
