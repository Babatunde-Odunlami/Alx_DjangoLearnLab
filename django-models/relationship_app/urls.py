#Edit relationship_app/urls.py to include URL patterns that route to the newly created views. Make sure to link both function-based and class-based views.

#import necessary packages
from django.urls import path
from .views import BookListView

#create url patterns
urlpatterns = [
    path('book_list/', views.book_list, name='book_list'),
    path('books/', BookListView.as_view(), name='book-list'),
]
