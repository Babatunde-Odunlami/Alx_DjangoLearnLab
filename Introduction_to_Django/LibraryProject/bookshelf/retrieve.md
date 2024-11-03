# retrieve.md
# Retrieve the Book instance == book
from bookshelf.models import Book
book = Book.objects.get(title="1984")
print(book)

# Expected output
# Book: 1984 by George Orwell, 1949
