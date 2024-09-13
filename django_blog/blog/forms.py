from django import forms
from django.contrib.auth.models import User
from .models import Post, Comment
from taggit.forms import TagWidget  # Import TagWidget for tag handling

# Form for updating user details
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

# Form for creating and updating blog posts
class PostForm(forms.ModelForm):
    tags = forms.CharField(
        required=False,
        widget=TagWidget()  # Use TagWidget to handle tags
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']  # Include 'tags' field

    def save(self, commit=True):
        post = super().save(commit=False)
        if commit:
            post.save()
            self.save_m2m()  # Save tags to many-to-many field
        return post

# Form for creating and updating comments
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }
