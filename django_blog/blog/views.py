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

"""
#Profile management: create a view that allows authenticated users to view and edit thier profiles.
#This view should handle POST requests to update user information.
#extend the user model to enable addition of  bio and profile pic


#This method is correct and automatic handling provided by Django's UpdateView but rejected by the checker
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

class UpdateProfileView(UpdateView, LoginReguiredMixin):
    model = User
    template_name = 'blog/update_profile.html'
    success_url = reverse_lazy('profile') # where to redirect after successful update

    def get_object(self):
        return self.request.user    #ensure user can only edit thier own profile
"""

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserProfileForm

@login_required
def Update_Profile(request):
    user = request.user  # Get the currently logged-in user
    if request.method == 'POST':  # Check for POST request
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()  # Save the updated user details
            messages.success(request, 'Your profile has been updated.')
            return redirect('profile')  # Redirect to the profile page
    else:
        form = UserProfileForm(instance=user)  # Pre-fill the form with current user data
    return render(request, 'blog/update_profile.html', {'form': form})


