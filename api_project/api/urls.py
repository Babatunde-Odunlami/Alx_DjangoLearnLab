from django.urls import path
from .views import BookList

#create urlpatterns

urlpatterns = [
        path('books/', BookList.as_view(), name = 'book-list'),
        ]
