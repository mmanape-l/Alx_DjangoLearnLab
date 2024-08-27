from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_date', 'isbn']
        
    def clean_isbn(self):
        isbn = self.cleaned_data.get('isbn')
        if isbn:
            # Remove any hyphens or spaces from the ISBN
            isbn = ''.join(c for c in isbn if c.isdigit())
            if len(isbn) != 10 and len(isbn) != 13:
                raise forms.ValidationError("ISBN must be either 10 or 13 digits.")
        return isbn

class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label="Your Name")
    email = forms.EmailField(required=True, label="Your Email")
    message = forms.CharField(widget=forms.Textarea, required=True, label="Your Message")
    age = forms.IntegerField(min_value=0, max_value=120, required=False, label="Your Age")
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and not email.endswith('@example.com'):
            raise forms.ValidationError("Please use an email address from example.com domain.")
        return email


