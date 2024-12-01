from django.db import models

# Create your models here.
#Task 0: creating the Author and Book Models
class Author(models.Model):
    '''creating the blueprint for Author instances'''
    name = models.CharField(max_length=100)

class Book(models.Model):
    '''creating a blueprint for Book instances'''
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
