from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_date = models.DateTimeField(auto_now=True)  # New field to track last update
    slug = models.SlugField(max_length=200, unique=True, blank=True)  # New field for SEO-friendly URLs

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)  # Automatically create slug from title
        super().save(*args, **kwargs)


