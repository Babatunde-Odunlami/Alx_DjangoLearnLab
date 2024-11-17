from django.shortcuts import render
#Task 1
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



#Task 2
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

#checks if user is authenticated and also the admin role
def is_admin(user):
    return user.userprofile.role == 'Admin'
#when the user check passes, test user again before user can access role-based view
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

#checks if user is authenticated and also the librarian role
def is_librarian(user):
    return user.userprofile.role == 'Librarian'
#when the user check passes, test user again before user can access role-based view
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

#checks if user is authenticated and also the member role
def is_member(user):
    return user.userprofile.role == 'Member'
#when the user check passes, test user again before user can access role-based view
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')




#TASK 4
# relationship_app/views.py
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect
from .models import Book


@permission_required('relationship_app.can_add_book')
def add_book(request):
    return render(request, 'relationship_app/add_book.html')

@permission_required('relationship_app.can_change_book')
def edit_book(request):
    return render(request, 'relationship_app/edit_book.html')

@permission_required('relationship_app.can_delete_book')
def delete_book(request):
    return render(request, 'relationship_app/delete_book.html')

