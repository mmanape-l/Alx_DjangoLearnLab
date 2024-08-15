from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

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

@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@login_required
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')


