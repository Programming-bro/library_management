from rest_framework.response import Response
from rest_framework import status
from books.models import Book, Category, Author
from books.serializers import BookSerializer, CategorySerializer, AuthorSerializer
from django.db.models import Count
from rest_framework.viewsets import ModelViewSet
from api.permissions import IsAdminOrLibrarianOrReadOnly
from drf_yasg.utils import swagger_auto_schema
# from api.permissions import IsAdminOrReadOnly

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminOrLibrarianOrReadOnly]

    @swagger_auto_schema(
        operation_summary='Retrive a list of books'
    )
    def list(self, request, *args, **kwargs):
        """Retrive all the books"""
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create a book by admin",
        operation_description="This allow an admin or librarian to create a books",
        request_body=BookSerializer,
        responses={
            201: BookSerializer,
            400: "Bad Request"
        }
    )
    def create(self, request, *args, **kwargs):
        """Only authenticated admin can create product"""
        return super().create(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_summary='Delete a specific book'
    )
    def destroy(self, request, *args, **kwargs):
        book = self.get_object()
        self.perform_destroy(book)
        return Response(status=status.HTTP_204_NO_CONTENT)
    @swagger_auto_schema(
        operation_summary='Retrive a specific book'
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_summary='Update a specific books'
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_summary='Paritally updates a specific books'
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.annotate(
    product_count=Count('books')).all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrLibrarianOrReadOnly]

    @swagger_auto_schema(
        operation_summary='Retrive a list of category'
    )
    def list(self, request, *args, **kwargs):
        """Retrive all the categories"""
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create a category by admin",
        
    )
    def create(self, request, *args, **kwargs):
        """Only authenticated admin can create category"""
        return super().create(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_summary='Delete a specific category'
    )
    def destroy(self, request, *args, **kwargs):
        category = self.get_object()
        self.perform_destroy(category)
        return Response(status=status.HTTP_204_NO_CONTENT)
    @swagger_auto_schema(
        operation_summary='Retrive a specific category'
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_summary='Update a specific category'
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_summary='Paritally updates a specific category'
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)


class AuthorViewSet(ModelViewSet):
    serializer_class = AuthorSerializer
    permission_classes = [IsAdminOrLibrarianOrReadOnly]

    def get_queryset(self):
        return Author.objects.all()
    @swagger_auto_schema(
        operation_summary='Retrive a list of author'
    )
    def list(self, request, *args, **kwargs):
        """Retrive all the author"""
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create a author by admin",
    )
    def create(self, request, *args, **kwargs):
        """Only authenticated admin can create author"""
        return super().create(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_summary='Delete a specific author'
    )
    def destroy(self, request, *args, **kwargs):
        author = self.get_object()
        self.perform_destroy(author)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    @swagger_auto_schema(
        operation_summary='Retrive a specific author'
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_summary='Update a specific author'
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_summary='Paritally updates a specific author'
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)