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
