from rest_framework.response import Response
from rest_framework import status
from books.models import Book, Category, Author
from books.serializers import BookSerializer, CategorySerializer, AuthorSerializer
from django.db.models import Count
from rest_framework.viewsets import ModelViewSet
from api.permissions import IsAdminOrLibrarianOrReadOnly
# from api.permissions import IsAdminOrReadOnly

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminOrLibrarianOrReadOnly]

    def destroy(self, request, *args, **kwargs):
        book = self.get_object()
        self.perform_destroy(book)
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.annotate(
    product_count=Count('books')).all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrLibrarianOrReadOnly]


class AuthorViewSet(ModelViewSet):
    serializer_class = AuthorSerializer
    permission_classes = [IsAdminOrLibrarianOrReadOnly]

    def get_queryset(self):
        return Author.objects.all()