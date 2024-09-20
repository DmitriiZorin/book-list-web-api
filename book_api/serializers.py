from rest_framework import serializers
from book_api import models

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = ['name', 'author', 'date_published']