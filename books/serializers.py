from rest_framework import serializers
from books.models import Book, Category, Author


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'description', 'book_count']

    book_count = serializers.IntegerField(read_only=True)


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'category',
                  'available_quantity'] 

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id','name','biography']
