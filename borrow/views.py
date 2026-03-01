from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from borrow.models import Borrow
from borrow.serializers import BorrowSerializer
from drf_yasg.utils import swagger_auto_schema

# Create your views here.

class BorrowViewSet(ModelViewSet):
    serializer_class = BorrowSerializer
    permission_classes = [permissions.IsAuthenticated] 

    def get_queryset(self):
        user = self.request.user
        if user.is_staff or user.is_superuser:
            return Borrow.objects.all()
        if user.groups.filter(name='Librarian').exists():
            return Borrow.objects.all()
        return Borrow.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @swagger_auto_schema(
        operation_summary='Retrive a list of borrows'
    )
    def list(self, request, *args, **kwargs):
        """Retrive all the borrows"""
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create a borrow by user",
    )
    def create(self, request, *args, **kwargs):
        """Only authenticated users can create borrow"""
        return super().create(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_summary='Delete a specific borrow'
    )
    def destroy(self, request, *args, **kwargs):
        borrow = self.get_object()
        self.perform_destroy(borrow)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    @swagger_auto_schema(
        operation_summary='Retrive a specific borrow'
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_summary='Update a specific borrow'
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_summary='Paritally updates a specific borrow'
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)