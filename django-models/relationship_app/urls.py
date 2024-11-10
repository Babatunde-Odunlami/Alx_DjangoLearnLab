#Edit relationship_app/urls.py to include URL patterns that route to the newly created views. Make sure to link both function-based and class-based views.

#import necessary packages
from django.urls import path
from .views import BookListView
from .views import list_books, LibraryDetailView
#create url patterns
urlpatterns = [
    path('list_books/', views.list_books, name='list-book'),
    path('book_list/', views.BookListView.as_view(), name = 'book_list')
    path('books/',LibraryDetailView.as_view(), name='book-list'),
]
