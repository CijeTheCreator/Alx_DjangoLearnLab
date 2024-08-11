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