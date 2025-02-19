# Delete Operation

**Objective:** Delete the book with the updated title and verify that it no longer exists.

**Command:**
```python
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
print(Book.objects.all())  # This should return an empty QuerySet if the deletion was successful.

