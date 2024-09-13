from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify  # Import slugify for generating slugs

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_date = models.DateTimeField(auto_now=True)  # Tracks the last time the post was updated
    slug = models.SlugField(max_length=200, unique=True, blank=True)  # SEO-friendly URLs based on the title

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Automatically generate a slug if it doesn't exist
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)  # Call the parent save method to save the model instance




