from django.shortcuts import render
from rest_framework import viewsets
from .models import Book
from rest_framework.permissions import IsAuthenticated
from .serializers import BookSerializer

#Create your views here.

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

