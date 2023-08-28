from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from app1.serializers import UserSerializer, GroupSerializer, usuariosSerializer
from .models import usuario #Importo mi modelo
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

class UsuariosViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited
    """
    queryset = usuario.objects.all()
    serializer_class = usuariosSerializer
    permission_classes = [permissions.IsAuthenticated]