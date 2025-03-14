from django.urls import path
from .views import BookListCreateView, BookRetrieveUpdateDestroyView

urlpatterns = [
    # List all books / Create a new book
    path('books/', BookListCreateView.as_view(), name='book-list-create'),

    # Retrieve / Update / Delete a specific book by ID
    path('books/<int:pk>/', BookRetrieveUpdateDestroyView.as_view(), name='book-detail'),
]

