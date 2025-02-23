# Retrieve Operation

**Objective:** Retrieve the book that was created and display all its attributes.

**Command:**
```python
book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)

