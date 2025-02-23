from django.urls import path
from . import views

urlpatterns = [
    # URL pattern for the function-based view (list all books)
    path('books/', views.list_books, name='list_books'),

    # URL pattern for the class-based view (display library details)
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]
