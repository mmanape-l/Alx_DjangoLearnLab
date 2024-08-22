from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Book

# Define the CustomUserAdmin class
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # Customize the admin interface for CustomUser if needed
    # For example:
    # fieldsets = (
    #     (None, {'fields': ('username', 'password')}),
    #     ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
    #     ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    #     ('Important dates', {'fields': ('last_login', 'date_joined')}),
    # )
    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('username', 'email', 'password1', 'password2'),
    #     }),
    # )
    # list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    # search_fields = ('username', 'email', 'first_name', 'last_name')
    # ordering = ('username',)

# Register the CustomUser model with the CustomUserAdmin class
admin.site.register(CustomUser, CustomUserAdmin)

# Define the BookAdmin class
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('author', 'publication_year')
    search_fields = ('title', 'author')

# Optionally, if you need to register the Book model without using the decorator:
# admin.site.register(Book, BookAdmin)
