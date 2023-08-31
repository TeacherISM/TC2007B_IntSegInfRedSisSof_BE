from django.shortcuts import render


# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from django.http import JsonResponse
from .models import directorio
from .serializers import UserSerializer, GroupSerializer, directorioSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

def home(request):
    return JsonResponse({'message': 'Hello World'})

class directorioViewSet(viewsets.ModelViewSet):
    ###
    # API endpoint that allows users to be viewed or edited.
    ###
    queryset = directorio.objects.all()
    serializer_class = directorioSerializer
    permission_classes = [permissions.IsAuthenticated]