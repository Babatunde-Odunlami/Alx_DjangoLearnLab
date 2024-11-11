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
class LoginView(auth_views.LoginView):
    template_name = 'relationship_app/login.html'

# Logout view
class LogoutView(auth_views.LogoutView):
    template_name = 'relationship_app/logout.html'

# Registration view
class register(CreateView):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'relationship_app/register.html', {'form': form)


#Task3
# relationship_app/views.py
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from django.http import HttpResponseForbidden

def Admin(user):
    return user.is_authenticated and user.userprofile.role == 'Admin'

def Librarian(user):
    return user.is_authenticated and user.userprofile.role == 'Librarian'

def Member(user):
    return user.is_authenticated and user.userprofile.role == 'Member'

@user_passes_test(Admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(Librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(Member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')


# relationship_app/views.py
def Admin(user):
    if user.is_authenticated:
        # Check if user has a UserProfile and the role is 'Admin'
        return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'
    return False






# relationship_app/views.py
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm

@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'relationship_app/add_book.html', {'form': form})

@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/edit_book.html', {'form': form, 'book': book})

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'relationship_app/delete_book.html', {'book': book})

