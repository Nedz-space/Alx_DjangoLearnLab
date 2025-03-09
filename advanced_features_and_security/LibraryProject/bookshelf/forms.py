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

class ExampleForm(forms.Form):
    # Simple form fields
    name = forms.CharField(max_length=100, required=True, label='Your Name')
    email = forms.EmailField(required=True, label='Your Email')
    message = forms.CharField(widget=forms.Textarea, required=True, label='Message')

    def clean_name(self):
        name = self.cleaned_data.get('name')
        # Basic sanitization: No special characters like < > { } etc.
        if any(char in name for char in ['<', '>', '{', '}', ';']):
            raise forms.ValidationError("Invalid characters in name.")
        return name

    def clean_message(self):
        message = self.cleaned_data.get('message')
        # Example check: limit length or filter out suspicious content
        if len(message) < 10:
            raise forms.ValidationError("Message is too short.")
        return message


# Optional: Leave in your existing BookForm and BookSearchForm too!
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'library']

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if any(char in title for char in ['<', '>', '{', '}']):
            raise forms.ValidationError("Invalid characters in title.")
        return title


class BookSearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False, label='Search Books')

    def clean_query(self):
        query = self.cleaned_data.get('query')
        if any(char in query for char in [';', '--', "'", '"']):
            raise forms.ValidationError("Invalid search query.")
        return query

