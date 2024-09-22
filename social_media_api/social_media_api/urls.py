"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', 'posts.urls')),  # Include the posts app URLs
]

