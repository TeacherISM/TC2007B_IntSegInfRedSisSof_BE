from rest_framework import viewsets, permissions
from django.contrib.auth.models import User, Group
from .serializers import UserSerializer, GroupSerializer

class UserViewSet(viewsets.ModelViewSet):  # Añadido ":" y corregido Modelviewset
    """
    API endpoint that allows users to be viewed or edited.
    """  # Corregido el comentario
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer  # Corregido el espacio en "serializer_ class"
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):  # Añadido ":"
    """
    API endpoint that allows groups to be viewed or edited.
    """  # Corregido el comentario
    queryset = Group.objects.all()
    serializer_class = GroupSerializer  # Corregido el espacio en "serializer class"
    permission_classes = [permissions.IsAuthenticated]
