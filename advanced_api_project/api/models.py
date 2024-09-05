
from django.db import models

class Author(models.Model):
    """
    Represents an author of books.
    
    This model stores information about authors, including their name.
    It has a one-to-many relationship with the Book model.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    Represents a book.
    
    This model stores information about books, including their title,
    publication year, and the author who wrote them. It has a many-to-one
    relationship with the Author model.
    """
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
