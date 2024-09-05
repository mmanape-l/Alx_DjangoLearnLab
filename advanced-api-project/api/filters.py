# api/filters.py
from django_filters import rest_framework as filters
from .models import Book

class BookFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')
    publication_year = filters.NumberFilter(lookup_expr='exact')
    author = filters.CharFilter(field_name='author__name', lookup_expr='icontains')

    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']
