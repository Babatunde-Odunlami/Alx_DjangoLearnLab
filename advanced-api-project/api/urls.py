from .views import BookList, BookDetail, BookCreate, BookUpdate, BookDelete
from django.urls import path
from rest_framework.routers import DefaultRouter

#create an instance of a routers.DefaultRouter
router =routers.DefaultRouter()

#register the BookViewSet with the router
#router.register(r'books', BookViewSet, basename='book')

urlspatterns = [
        path('books/', BookList.as_view(), name ='booklist'),
        path('books/<int:pk>/', BookDetail.as_view(), name ='bookdetail'),
        path('books/create/', BookCreate.as_view(), name = 'bookcreate'),
        path('books/update/<int:pk>/', BookUpdate.as_view(), name = 'bookupdate'),
        path('books/delete/,int:pk>?', BookDelete.as_view(), name= 'bookdelete'),
        ]
