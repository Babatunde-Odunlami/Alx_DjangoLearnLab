from django.shortcuts import render
from .models import CustomUserCreationForm  #needed to register new users
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView


# Create your views here.

#register view
class register(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'blog/register.html'


#profile view
class ProfileView(TemplateView):
    template_name = 'blog/profile.html'
