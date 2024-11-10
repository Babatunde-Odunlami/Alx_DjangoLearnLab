#import necessary packages
from django.urls import path
from .views import BookListView

#create url patterns
urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
]
