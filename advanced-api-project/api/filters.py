from django-filter import django_filters
from .models import Book

class BookFilter(django_filters.FilterSet):
    class Meta:
        model = Book
        fields = {
                {'title': ['exact', 'icontains'],  # Filter for exact matches and partial matches
                    'author': ['exact', 'icontains'], 
                    'publication_year': ['exact', 'gte', 'lte'],  # Range filtering 
                    }
                }
