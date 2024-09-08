# Book API

## Endpoints

- `/books/`: List all books.
- `/books/<id>/`: Retrieve details for a specific book.
- `/books/create/`: Create a new book (authenticated users only).
- `/books/<id>/update/`: Update a book (authenticated users only).
- `/books/<id>/delete/`: Delete a book (authenticated users only).

## Permissions

- Unauthenticated users can view books.
- Only authenticated users can create, update, or delete books.

## API Query Features

### Filtering

You can filter books by `title`, `author name`, or `publication year`.
Example:
/api/books/?title=SomeTitle&author\_\_name=SomeAuthor&publication_year=2020

### Searching

You can search books by `title` or `author name`.
Example:
/api/books/?search=SomeQuery

### Ordering

You can order books by `title` or `publication year`.
Example:
/api/books/?ordering=title

Copy code

## Running Tests

To run the tests for the API, use the following command:
python manage.py test api
