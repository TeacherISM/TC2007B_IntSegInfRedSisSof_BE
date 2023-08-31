from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from SEL4C.app1.serializers import UserSerializer, GroupSerializer
from django.http import JsonResponse
from .models import HomeModel
from .serializers import HomeSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]  

class HomeViewSet(viewsets.ModelViewSet):
    queryset = HomeModel.objects.all()
    serializer_class=HomeSerializer
    permission_classes=[permissions.IsAuthenticated]

def home(request):
    return JsonResponse({'message':'HelloWorld'})
