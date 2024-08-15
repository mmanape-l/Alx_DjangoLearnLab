from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.auth import login
from django.shortcuts import redirect

class CustomLoginView(LoginView):
    template_name = 'login.html'
    
    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.get_user()
        login(self.request, user)
        return response

class CustomLogoutView(LogoutView):
    template_name = 'logout.html'

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        return response

