# Create a Book Instance

```python
from bookshelf.models import Book

# Creating a new Book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book.save()

# Expected output
# <Book: 1984>
```
