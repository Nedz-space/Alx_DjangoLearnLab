#Admin.py

from django.contrib import admin
from .models import Book, Author, Library

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Ensure publication_year exists
    list_filter = ('author', 'publication_year')
    search_fields = ('title', 'author__name')  # Fix for ForeignKey

admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Library)

