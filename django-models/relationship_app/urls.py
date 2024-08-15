from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import user_register

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/', user_register, name='register'),
]
