# Delete the Book Instance

```python
from bookshelf.models import Book
retrieved_book = Book.objects.get(title="1984")
# Deleting the book
retrieved_book.delete()

# Expected output:
# <QuerySet []>
```