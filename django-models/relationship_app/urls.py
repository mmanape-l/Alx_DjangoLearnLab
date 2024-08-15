from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views  # Ensure this import is correct

urlpatterns = [
    # URL pattern for user login
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),

    # URL pattern for user logout
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),

    # URL pattern for user registration
    path('register/', views.register, name='register'),  # Matches exactly to views.register
]
