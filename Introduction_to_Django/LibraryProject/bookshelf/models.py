from django.db import models

# Create your models here.
class Book(models.Model):
    '''attributes of a Book'''
    title = models.CharField(max=200)
    author = models.CharField(max=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return f"{self.title} by {self.author} {self.publication_year}"
