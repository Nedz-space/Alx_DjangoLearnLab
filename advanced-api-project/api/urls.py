from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
)

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),                  # GET all books
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),     # GET single book by id
    path('books/create/', BookCreateView.as_view(), name='book-create'),       # POST new book
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name='book-update'),   # PUT/PATCH update existing book
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='book-delete'),   # DELETE existing book
]

