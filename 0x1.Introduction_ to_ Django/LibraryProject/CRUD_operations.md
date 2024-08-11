# Create a Book Instance

```python
from bookshelf.models import Book

# Creating a new Book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book.save()

# Expected output
# <Book: 1984>
```

# Retrieve the Book Instance

```python
# Retrieving the book by title
retrieved_book = Book.objects.get(title="1984")
retrieved_book

# Expected output:
# <Book: 1984>
# Attributes:
# title: 1984
# author: George Orwell
# publication_year: 1949
```

# Update the Book Title

```python
# Updating the book's title
retrieved_book.title = "Nineteen Eighty-Four"
retrieved_book.save()

# Expected output:
# <Book: Nineteen Eighty-Four>
```

# Delete the Book Instance

```python
# Deleting the book
retrieved_book.delete()

# Expected output:
# <QuerySet []>
```