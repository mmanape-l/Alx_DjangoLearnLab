from rest_framework import serializers
from .models import Author, Book
from django.utils import timezone

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        if value > timezone.now().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    book_count = serializers.SerializerMethodField()

    class Meta:
        model = Author
        fields = ['id', 'name', 'books', 'book_count']

    def get_book_count(self, obj):
        return obj.books.count()
