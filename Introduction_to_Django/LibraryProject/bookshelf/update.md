# Update Operation

**Objective:** Update the title of the book "1984" to "Nineteen Eighty-Four" and save the changes.

**Command:**
```python
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
print(book)

