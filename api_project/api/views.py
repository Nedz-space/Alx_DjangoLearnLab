# Create your views here.

from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()  # Get all book instances
    serializer_class = BookSerializer  # Use the BookSerializer to serialize them

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can access
    permission_classes = [IsAdminUser]  # Only admins can CRUD books

