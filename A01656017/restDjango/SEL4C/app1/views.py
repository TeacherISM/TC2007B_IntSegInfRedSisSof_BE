from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .models import Emprendedor
from .serializers import EmprendeSerializer
from SEL4C.app1.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    permission_classes = [permissions.IsAuthenticated]
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class EmprendeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Entrepreneurs to be viewed or edited.
    """
    permission_classes = [permissions.IsAuthenticated]
    queryset = Emprendedor.objects.all()
    serializer_class = EmprendeSerializer