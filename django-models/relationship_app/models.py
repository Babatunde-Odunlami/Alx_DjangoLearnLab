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


# relationship_app/models.py
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='Member')

    def __str__(self):
        return f"{self.user.username} - {self.role}"

# Signal to automatically create a UserProfile
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.
