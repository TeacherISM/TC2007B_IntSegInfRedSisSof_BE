from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from app1.serializers import UserSerializer, GroupSerializer
from .models import cliente
from .serializers import ClienteSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class clienteViewSet(viewsets.ModelViewSet):
    """
    Api endpoint that allows users to be viewed or edited
    """
    queryset = cliente.objects.all()

    serializer_class = ClienteSerializer
    permission_classes = [permissions.IsAuthenticated]
    