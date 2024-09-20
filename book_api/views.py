from django.shortcuts import render
from rest_framework import generics, permissions
from book_api import models
from book_api import serializers

# Create your views here.

class BookList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer