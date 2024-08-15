from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    # URL pattern for user login
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    
    # URL pattern for user logout
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    
    # URL pattern for user registration
    path('register/', views.register, name='register'),
    
    # URL patterns for role-based views
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
]