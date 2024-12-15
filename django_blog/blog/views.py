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
class ProfileView(TemplateView):i
    template_name = 'blog/profile.html'


#Profile management: create a view that allows authenticated users to view and edit thier profiles.
#This view should handle POST requests to update user information.
#extend the user model to enable addition of  bio and profile pic

from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

class UpdateProfileView(UpdateView, LoginReguiredMixin):
    model = User
    template_name = 'blog/update_profile.html'
    success_url = reverse_lazy('profile') # where to redirect after successful update

    def get_object(self):
        return self.request.user    #ensure user can only edit thier own profile
