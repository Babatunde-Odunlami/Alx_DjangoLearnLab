from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#function based view
def book_list(request):
    books = Book.objects.all()
    context = {'book_list': books}
    return render(request,'relationship_app/list_books.html', context)

#class based view
from django.views.generic import ListView
from .models import Book

class BookListView(ListView):
    model = Book
    template_name = library_detail.html
    context_object_name = books


