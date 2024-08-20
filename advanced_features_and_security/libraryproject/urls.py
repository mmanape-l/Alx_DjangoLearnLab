from django.contrib import admin
from django.urls import path, include  # Import 'include' to include app URLs

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin site URL
    path('relationship/', include('relationship_app.urls')),  # Include URLs from the relationship_app
]
