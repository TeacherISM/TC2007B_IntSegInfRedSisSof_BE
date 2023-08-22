from django.contrib.auth.models import User, Group
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModeSerializer):
	class Meta:
		model = User
		fields = ['url', 'username', 'email', 'group']

class GroupSerializer(serializers.HyperlinkedModeSerializer):
	class Meta:
		model = Group
		fields = ['url', 'name']
