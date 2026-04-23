from rest_framework.viewsets import ModelViewSet
from library.models import User
from library.serializers import UserSerializer
from library.permissions import IsAdminOnly




class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminOnly]