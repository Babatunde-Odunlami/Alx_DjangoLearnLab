from django.db import models

# Create your models here.
#create the AuthorModel
class Author(models.Model)
    name = models.charField(max_length = 100)
    def __str__(self):
        return self.name

#create the BookModel
class Book(models.Model)
    title = models.charField(max_length = 100)
    authors = models.ForeignKey(Author, on_delete = models.CASCADE, related_name='boo')

#create LibraryModel
class Library(models.Model)
    name = models.charField(max_length = 100)
    books = models.ManyToManyField(Book, related_named='library')

#create LibrarianModel
class Librarian(models.Model)
    name = models.charField(max_length = 100)
    libraries = models.OneToOneField(Library, on_delete= models.CASCADE, related_named='librarian')
