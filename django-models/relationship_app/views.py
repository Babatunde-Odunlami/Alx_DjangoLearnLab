from django.shortcuts import render

# Create your views here.
#function based view
def list_books(request):
    books = Book.objects.all()
    context = {'book_list': books}
    return render(request,'relationship_app/list_books.html', context)

#class based view
#Create a class-based view in relationship_app/views.py that displays details for a specific library,listing all books available in the library.
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Library

#Utilize Django's ListView or DetailView to structure this class-based view.

class BookListView(ListView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = books

#Utilize Django's ListView or DetailView to structure this class-based view.
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = books


# relationship_app/views.py
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login
# Login view
class Login(auth_views.LoginView):
    template_name = 'relationship_app/login.html'

# Logout view
class Logout(auth_views.LogoutView):
    template_name = 'relationship_app/logout.html'

# Registration view
class Register(CreateView):
    form_class = UserCreationForm
    template_name = 'relationship_app/register.html'
    success_url = reverse_lazy('login')

