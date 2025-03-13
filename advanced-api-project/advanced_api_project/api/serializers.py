from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):
    """
    BookSerializer serializes the Book model.
    Includes custom validation to ensure publication_year is not in the future.
    """
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        """
        Custom validation to ensure publication_year is not in the future.
        """
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError(f"Publication year cannot be in the future. Current year is {current_year}.")
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """
    AuthorSerializer serializes the Author model and nests the BookSerializer.
    The 'books' field shows all books associated with this author.
    """
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']

