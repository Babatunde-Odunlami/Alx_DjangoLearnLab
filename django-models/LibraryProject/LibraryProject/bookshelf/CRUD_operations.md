#CRUD_operations.md

#create.md
from bookshelf.models import Book
# Create an instance from the Book class (model)
book = Book.objects.create(title ="1984", author="George Orwell", publication_year= 1949)
print(book)
# Expected output
# Book: 1984 by George Orwell, 1949


#retrieve.md
# Retrieve the Book instance == book
from bookshelf.models import Book
book = Book.objects .get(title="1984")
print(book)
# Expected output
# Book: 1984 by George Orwell, 1949


#update.md
# Update the Book instance == book
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
# Retrieve updated book to confirm the change
updated_book = Book.objects.get(title="Nineteen Eighty-Four")
print(updated_book)
# Expected output
# Book: Nineteen Eighty-Four by George Orwell, 1949


#delete.md
from bookshelf.models import Book
# Delete the Book instance == book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
# Confirm "book" is deleted
all_books = Book.objects.all()
print(all_books) 
# Expected output
# [] -- empty list
