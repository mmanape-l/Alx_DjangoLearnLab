from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),  # Include the accounts app URLs
    path('api/posts/', include('posts.urls')),  # Include the posts app URLs
]

