from rest_framework.viewsets import ModelViewSet
from borrow.models import Member
from users.serializers import MemberSerializer

# Create your views here.

class MemberViewSet(ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    def destroy(self, request, *args, **kwargs):
        member = self.get_object()
        self.perform_destroy(member)
        return Response(status=status.HTTP_204_NO_CONTENT)