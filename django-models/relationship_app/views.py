from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView

# Custom registration view
class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

# Custom login view
class CustomLoginView(LoginView):
    template_name = 'login.html'

# Custom logout view
class CustomLogoutView(LogoutView):
    template_name = 'logout.html'

