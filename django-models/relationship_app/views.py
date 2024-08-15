from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth import login

# Custom LoginView
class CustomLoginView(LoginView):
    template_name = 'login.html'  # Ensures the login template is used

# Custom LogoutView
class CustomLogoutView(LogoutView):
    template_name = 'logout.html'  # Ensures the logout template is used

# Custom RegisterView using CreateView
class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'  # Ensures the registration template is used
    success_url = reverse_lazy('login')  # Redirect to login after registration

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        login(self.request, user)  # Log in the user after registration
        return response

# Role-based views
def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, "admin_view.html")

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, "librarian_view.html")

@user_passes_test(is_member)
def member_view(request):
    return render(request, "member_view.html")


