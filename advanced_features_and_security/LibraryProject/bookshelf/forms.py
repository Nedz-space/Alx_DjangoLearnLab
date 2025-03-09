from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'library']

    def clean_title(self):
        title = self.cleaned_data.get('title')
        # Example of sanitizing and validating
        if any(char in title for char in ['<', '>', '{', '}']):
            raise forms.ValidationError("Invalid characters in title.")
        return title

class BookSearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False, label='Search Books')

    def clean_query(self):
        query = self.cleaned_data.get('query')
        # Simple validation to avoid special characters
        if any(char in query for char in [';', '--', "'", '"']):
            raise forms.ValidationError("Invalid search query.")
        return query

