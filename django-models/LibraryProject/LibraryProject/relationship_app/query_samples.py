from relationship_app.models import Author, Book, Libary, Librarian
#query all books by a specific Author
author = Author.objects.get(name=author_name)
books = Book.select_related(author)
books = Book.objects.filter(author=author)

#list all books in a library
library = Library.objects.get(name=library_name)
books = Book.objects.prefetch_related('library')
books.all()

#retrieve the librarian for a library
librarian = Librarian.objects.get(library="library")


