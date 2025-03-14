from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

# Serializer for the Book model
class BookSerializer(serializers.ModelSerializer):

    # Custom validation for publication_year
    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']


# Serializer for the Author model, including nested books
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']

