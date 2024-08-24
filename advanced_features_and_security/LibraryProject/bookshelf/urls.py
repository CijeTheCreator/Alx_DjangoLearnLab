from django.urls import path
from .views import book_details, book_list, create_book, edit_book, delete_book

urlpatterns = [
    path("book_list", book_list, name="book_list"),
    path("book_details/<int:pk>", book_details, name="book_details"),
    path("create_book", create_book, name="create_book"),
    path("edit_book/<int:pk>", edit_book, name="edit_book"),
    path("delete_book/<int:pk>", delete_book, name="delete_book"),
]