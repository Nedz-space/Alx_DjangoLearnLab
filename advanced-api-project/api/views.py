# Create your views here.

from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# ------------------------------
# List and Create View for Books
# ------------------------------
class BookListCreateView(generics.ListCreateAPIView):
    """
    GET: List all books (accessible to everyone)
    POST: Create a new book (authenticated users only)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Permissions: Allow anyone to view, but only authenticated users to create
    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]


# ------------------------------
# Retrieve, Update, Delete View for Books
# ------------------------------
class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: Retrieve book details (accessible to everyone)
    PUT/PATCH: Update a book (authenticated users only)
    DELETE: Delete a book (authenticated users only)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Permissions: Allow read-only to anyone, modifications to authenticated users
    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]
