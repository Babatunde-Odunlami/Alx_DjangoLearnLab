from django.urls import path
from . import views    #register and profile views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
        path('login/', LoginView.as_view(template_name = 'blog/login.html'), name = 'Login'),
        path('logout/', LogoutView.as_view(template_name = 'blog/logout.html'), name= 'Logout'),
        path('register/', views.register.as_view(), name = 'Register'),
        path('profile/', views.ProfileView.as_view(), name = 'Profile'),
        path('update_profile/', views.UpdateProfileView.as_view(), name = 'Update'),
        ]
