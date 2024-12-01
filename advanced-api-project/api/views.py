from django.shortcuts import render

from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend, SearchFilter, OrderingFilter
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer
from .filters import BookFilter  #import from the created filters.py file
from rest_framework.filters import SearchFilter

# Create your views here.
class BookListView(generics.ListAPIView):
    ''' assign objects to attributes'''
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = BookFilter
    search_fields = ['title', 'author']   #these would be the only serachbale fields
    ordering_fields = ['title', 'publication_year']  #fileds that can be used to order the objects
    ordering = ['title'] # default field of order or sorting objects of Book
