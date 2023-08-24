from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from SEL4C.app1.serializers import UserSerializer, GroupSerializer
from .models import catCreate ##Importamos mi modelo
from .serializers import catSerializer ##Importamos al serializer

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_clasesses = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class CatViewSet(viewsets.ModelViewSet):
    """
    API enpoint that allow for edition or viewed
    """

    queryset = catCreate.objects.all() ##For the view enabling
    serializer_call= catSerializer ##Set the serializer class
    permission_classes= [permissions.IsAuthenticated] ##Set the permission
