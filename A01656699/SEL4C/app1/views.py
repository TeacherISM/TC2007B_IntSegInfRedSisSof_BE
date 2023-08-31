from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from SEL4C.app1.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

from .models import UsuarioModel  # Import your model
from .serializers import UsuarioSerializer # Import your serializer

class UsuarioViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows MyModel to be viewed or edited.
    """
    queryset = UsuarioModel.objects.all()  # Set the queryset for the view
    serializer_class = UsuarioSerializer  # Set the serializer class
    permission_classes = [permissions.IsAuthenticated]  # Set the permission classes