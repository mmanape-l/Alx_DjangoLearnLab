from django.urls import reverse_lazy
from django.contrib.auth.views import loginView
from django.contrib.auth.views import logoutView
from django.views.generic.edit import createView
from django.contrib.auth.forms import userCreationForm

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
