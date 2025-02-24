import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author using objects.filter()
def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)  # Using filter to get books by author
        print(f"Books by {author_name}:")
        for book in books:
            print(book.title)
    except Author.DoesNotExist:
        print(f"Author '{author_name}' not found.")

# List all books in a library
def get_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()  # Using ManyToMany relationship
        print(f"Books in {library_name}:")
        for book in books:
            print(book.title)
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")

# Retrieve the librarian for a library using Librarian.objects.get()
def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)  # Using get() to retrieve the librarian
        print(f"Librarian for {library_name}: {librarian.name}")
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")
    except Librarian.DoesNotExist:
        print(f"No librarian found for {library_name}.")

# Example usage
if __name__ == "__main__":
    # Query all books by a specific author
    get_books_by_author("J.K. Rowling")

    # List all books in a library
    get_books_in_library("Central Library")

    # Retrieve the librarian for a library
    get_librarian_for_library("Central Library")
