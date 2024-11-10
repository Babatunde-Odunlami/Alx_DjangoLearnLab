from relationship_app.models import Author, Book, Libary, Librarian
#query all books by a specific Author
books = Book.objects.select_related('author')

#list all books in a library
library = Libary.objects.get(name='library_name')
books = Book.objects.prefetch_related('library')
books.all()

#retrieve the librarian for a library
librarian = Librarian.objects.get(library="library")


