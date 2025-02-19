# Create Operations for Book Model

## Create Operation

**Objective:** Create a Book instance with the following details:  
- **Title:** "1984"  
- **Author:** "George Orwell"  
- **Publication Year:** 1949

**Command:**
```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)

---

## Retrieve Operation

**Objective:** Retrieve the book that was created and display all its attributes.

**Command:**
```python
book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)

---

## Update Operation

**Objective:** Update the title of the book "1984" to "Nineteen Eighty-Four" and save the changes.

**Command:**
```python
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
print(book)

---

## Delete Operation

**Objective:** Delete the book with the updated title and verify that it no longer exists.

**Command:**
```python
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
print(Book.objects.all())  # This should return an empty QuerySet if the deletion was successful.
