# delete.md
from bookshelf.models import Book
#Delete the Book instance == book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

#Confirm "book" is deleted
all_books = Book.objects.all()
print(all_books) 

# Expected output
# [] -- empty list
