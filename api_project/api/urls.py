from django.urls import path
from .views import BookList
#Task 2
from .views import BookViewSet
from rest_framework.routers import DefaultRouter
from django.urls import include
#create urlpatterns

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename = 'book_all')

urlpatterns = [
        #task1: Route for BookList View (ListViewAPI)
        path('books/', BookList.as_view(), name = 'book-list'),
        #task2: Include the generated router URLS for BookViewSet (all CRUD operations)
        path('', include(router.urls)), #includes all routes registered with the router
        ]
