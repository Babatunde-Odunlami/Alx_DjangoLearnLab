from django.shortcuts import render
#task 1
from rest_framework import generics
from django_filters import rest_framework #import DjangoFilterBackend, SearchFilter, OrderingFilter
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer
from .filters import BookFilter  #import from the created filters.py file
from rest_framework.filters import SearchFilter
#import the necessary generics .APIS to perform CRUD operations
from rest_framework.generics import ListView, ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
#import necessary authentication toolss
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated


# Create your views here.
class BookList(generics.ListAPIView):
    #check for authentication or if the field is just to read only without authentication
    permission_classes = [IsAuthenticatedOrReadOnly]
    ''' assign objects to attributes'''
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [rest_framework.DjangoFilterBackend, rest_framework.SearchFilter]
    filterset_class = BookFilter
    search_fields = ['title', 'author']   #these would be the only serachbale fields
    ordering_fields = ['title', 'publication_year']  #fileds that can be used to order the objects
    ordering = ['title'] # default field of order or sorting objects of Book

# A DetailView of  a single book
class BookDetail(RetrieveAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Book.objects.all() 
    serializer_class = BookSerializer

# A CreateView for adding a new book.
class BookCreate(CreateAPIView):
    permission_classes = [IsAuthenticated]  #require to track who added book
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def create_book(self, request, *args, **kwargs):
        # check that the title of the book is not greater than 5 characters
        if len(request.data.get('title', '')) < 2:
            return Response({'error: The title must be greater than 2 characters'}, status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)

    def save_book(self, serializer):
        serializer.save()


# An UpdateView for modifying an existing book.
class BookUpdate(UpdateAPIView):

    permission_classes = [IsAuthenticed]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        # Deserialize the data from the front end form
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)
        # return super().update(request, *args, **kwargs)

    def perform_update(self, serializer):
        serializer.save()

# A DeleteView for removing a book.
class BookDelete(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
