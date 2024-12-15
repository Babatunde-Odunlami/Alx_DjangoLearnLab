from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

#User = get_user_model()
 
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length =200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')


#customise usercreation form to have email field
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required = True, help_text="Required. Enter a valid email address.")
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'repeat_password']

    def save(self, commit=True):
        user = super().save(commit=False) #save the basic user instance first
        user.email =self.cleaned_data['email'] #set email field
        if commit:
            user.save() #save the user to the database
        return user


#create user profiles a with email extension
class Profile(models.Model):
    class Roles(models.TextChoices):
        member = "Member"
        admin = "Admin"

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = 'profiles')
    role = models.CharField(max_length=20, choices=Roles, default=Roles.member)
    email = models.EmailField()

    def __str__(self) -> str:
        return f"{self.user.username}'s profile."





from django.db import models 
# from django.contrib.auth.models import User # type: ignore
from django.contrib.auth import get_user_model
from taggit.managers import TaggableManager
User = get_user_model()
from django.utils.text import slugify


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', default="")
    tags = TaggableManager()
    
    def __str__(self):
        return self.title
    
  
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
    
    def __str__(self):
        return f"{self.author.username}'s Comment on {self.post}"
    
class Tag(models.Model):
    # name = models.ManyToManyField(Post, though='TagPost', blank=True)
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True, default='')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    
    
    def __str__(self):
        return self.name
    
class TagPost(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.tag}-{self.post}'
    
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=1000, null=True, blank=True, default='my bio')
    profile_pic = models.ImageField(null=True, blank=True, default='profile picture', upload_to='profile_pics/')
    
    def __str__(self):
        return f'{self.user.username} Profile'
