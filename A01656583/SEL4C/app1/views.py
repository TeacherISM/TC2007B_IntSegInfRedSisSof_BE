from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from SEL4C.app1.serializers import UserSerializer, GroupSerializer

class UserViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows users to be views or edited
	"""
	queryset = User.objects.all().order_by('-date_joined')
	serializer_class = UserSerializer
	permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows groups to be viewed or edited
	"""
	queryset = Group.objects.all()
	serializer_class = GroupSerializer
	permission_classes = [permissions.IsAuthenticated]

from .models import ActivityModel 				# Import your model
from .serializers import ActivitySerializer 	# Import your serializer

class HomeViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows MyModel to be viewed or edited
	"""
	queryset = ActivityModel.objects.all() 				# Set the queryset for the view
	serializer_class = ActivitySerializer 				# Set the serializer class
	permission_classes = [permissions.IsAuthenticated]	# Set the permissions classes