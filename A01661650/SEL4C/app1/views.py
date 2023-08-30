from django.contrib.auth.models import User, Group
from .models import Usuario, Admin
from rest_framework import viewsets
from rest_framework import permissions
from SEL4C.app1.serializers import UserSerializer, GroupSerializer, AdminSerializer, UsuarioSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows user to be viewed or edited
    """

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows user to be viewed or edited
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class UsuarioViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows user to be viewed or edited
    """

    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.IsAuthenticated]

class AdminViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows user to be viewed or edited
    """

    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
    permission_classes = [permissions.IsAuthenticated]
