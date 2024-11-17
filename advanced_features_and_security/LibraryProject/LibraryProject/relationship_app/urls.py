#Edit relationship_app/urls.py to include URL patterns that route to the newly created views. Make sure to link both function-based and class-based views.

#import necessary packages
from django.urls import path
from .views import BookListView
from .views import list_books, LibraryDetailView
from .views import Login, Logout, Register
from django.contrib.auth.views import LoginView, LogoutView
from .views import register
from .views import admin_view, librarian_view, member_view
from .views import add_book, edit_book, delete_book

#create url patterns
urlpatterns = [
    path('list_books/', views.list_books, name='list-book'),
    path('book_list/', views.BookListView.as_view(), name = 'book_list'),
    path('books/',LibraryDetailView.as_view(), name='book-list'), 
    path('login/', Login.as_view(), name='login'), 
    path('logout/', Logout.as_view(), name='logout'), 
    path('register/', views.Register.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('admin-view/', admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'),
    path('add_book/', add_book, name='add_book'),
    path('edit_book/<int:pk>/', edit_book, name='edit_book'),
    path('delete-book/<int:pk>/', delete_book, name='delete_book'),
    path('add_book/', add_book, name='add_book'),
    path('edit_book/', edit_book, name='edit_book'),
]
