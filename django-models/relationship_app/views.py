from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

# Custom LoginView
class CustomLoginView(LoginView):
    template_name = 'login.html'  # Ensures the login template is used

# Custom LogoutView
class CustomLogoutView(LogoutView):
    template_name = 'logout.html'  # Ensures the logout template is used

# Custom RegisterView using CreateView
class RegisterView(CreateView):
    form_class = UserCreationForm()
    template_name = 'register.html'  # Ensures the registration template is used
    success_url = reverse_lazy('login')  # Redirect to login after registration

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        login(self.request, user)  # Log in the user after registration
        return response

