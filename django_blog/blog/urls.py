from django.urls import path
from . import views .   #register and profile views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
        path('login/', LoginView.as_view(template_name = 'blog/login.html'), name = 'login'),
        path('logout/', LogoutView.as_view(template_name = 'blog/logout.html'), name= 'logout'),
        path('register/', views.register.as_view(), name = 'register'),
        path('profile/', views.ProfileView.as_view(), name = 'profile'),
        ]
