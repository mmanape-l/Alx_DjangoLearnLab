from django.urls import path
from . import views  # Ensure this import is correct

urlpatterns = [
    # URL pattern for user login
    path('login/', views.CustomLoginView.as_view(), name='login'),
    
    # URL pattern for user logout
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    
    # URL patterns for user registration
    path('register/', views.RegisterView.as_view(), name='register'),
    path('register/', views.register, name='register_func'),  # Add this line
    
    # URL patterns for role-based views
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
]