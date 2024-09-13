from django import forms
from django.contrib.auth.models import User
from .models import Post, Comment, Tag

# Form for updating user details
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

# Form for creating and updating blog posts
class PostForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple
    )
    
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 10, 'cols': 80}),
        }

# Form for creating and updating comments
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }
