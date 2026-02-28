from rest_framework.viewsets import ModelViewSet
from borrow.models import Borrow
from borrow.serializers import BorrowSerializer

# Create your views here.

class BorrowViewSet(ModelViewSet):
    queryset = Borrow.objects.all()
    serializer_class = BorrowSerializer

    def destroy(self, request, *args, **kwargs):
        borrow = self.get_object()
        self.perform_destroy(borrow)
        return Response(status=status.HTTP_204_NO_CONTENT)