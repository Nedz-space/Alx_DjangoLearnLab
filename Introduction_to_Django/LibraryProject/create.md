# Create Operation

**Objective:** Create a Book instance with the following details:  
- **Title:** "1984"  
- **Author:** "George Orwell"  
- **Publication Year:** 1949

**Command:**
```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)
