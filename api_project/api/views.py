# Create your views here.

from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework.generics import ListAPIView

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()  # Get all book instances
    serializer_class = BookSerializer  # Use the BookSerializer to serialize them

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
