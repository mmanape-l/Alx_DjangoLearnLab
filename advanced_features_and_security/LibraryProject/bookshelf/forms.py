from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_date']
        widgets = {
            'publication_date': forms.DateInput(attrs={'type': 'date'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'placeholder': 'Book Title'})
        self.fields['author'].widget.attrs.update({'placeholder': 'Author Name'})
        self.fields['publication_date'].widget.attrs.update({'placeholder': 'Publication Date'})
