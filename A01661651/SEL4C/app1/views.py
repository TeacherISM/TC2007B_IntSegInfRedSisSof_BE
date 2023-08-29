from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from SEL4C.app1.serializers import UserSerializer, GroupSerializer
from .models import HomeModel   # Import your model
from .serializers import HomeSerializer # Import your Serializer

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    """
    API EP
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API EP
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class HomeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows MyModel to be viewed or edited.
    """
    queryset = HomeModel.objects.all()  # Set the queryset for the view
    serializer_class = HomeSerializer # Set the serializer class
    permission_classes = [permissions.IsAuthenticated]  # Set the permissions classes
