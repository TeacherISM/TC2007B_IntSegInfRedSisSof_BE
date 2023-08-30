from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from SEL4C.app1.serializers import UserSerializer, GroupSerializer
from .models import RecetaModel
from .serializers import RecetaSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class RecetaViewSet(viewsets.ModelViewSet):
    queryset = RecetaModel.objects.all()
    serializer_class = RecetaSerializer
    permission_classes = [permissions.IsAuthenticated]


