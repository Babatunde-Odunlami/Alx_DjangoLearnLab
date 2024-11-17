# update.md
#Update the Book instance == book
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

# Retrieve updated book to confirm the change
updated_book = Book.objects.get(title="Nineteen Eighty-Four")
print(updated_book)

# Expected output
# Book: Nineteen Eighty-Four by George Orwell, 1949
