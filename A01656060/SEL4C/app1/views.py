from django.shortcuts import render
from django.contrib.auth.models import User, Group	
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer, ActivitySerializer, AdvanceSerializer, RetroSerializer
from .models import ActivityModel, AdvanceModel, RetroModel

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows users to be viewed or edited.
    '''
    queryset=User.objects.all().order_by('-date_joined')
    serializer_class=UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows groups to be viewed or edited.
    '''
    queryset=Group.objects.all()
    serializer_class=GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class ActivityViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows groups to be viewed or edited.
    '''
    queryset=ActivityModel.objects.all()
    serializer_class=ActivitySerializer
    permission_classes = [permissions.IsAuthenticated]

class AdvanceViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows groups to be viewed or edited.
    '''
    queryset=AdvanceModel.objects.all()
    serializer_class=AdvanceSerializer
    permission_classes = [permissions.IsAuthenticated]

class RetroViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows groups to be viewed or edited.
    '''
    queryset=AdvanceModel.objects.all()
    serializer_class=AdvanceSerializer
    permission_classes = [permissions.IsAuthenticated]