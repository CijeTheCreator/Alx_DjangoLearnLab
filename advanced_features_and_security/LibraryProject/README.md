# Permissions and Groups Setup

This project uses Django's built-in permissions system to control access to various parts of the application.

## Permissions

The following custom permissions have been defined for the Book model:

- `can_view`: Allows viewing book details
- `can_create`: Allows creating new books
- `can_edit`: Allows editing existing books
- `can_delete`: Allows deleting books

## Groups

Three user groups have been set up with the following permissions:

1. Viewers:
   - can_view

2. Editors:
   - can_view
   - can_create
   - can_edit

3. Admins:
   - can_view
   - can_create
   - can_edit
   - can_delete

