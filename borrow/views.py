from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from borrow.models import Borrow
from borrow.serializers import BorrowSerializer

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