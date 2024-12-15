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
