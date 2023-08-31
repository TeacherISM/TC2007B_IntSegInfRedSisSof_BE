from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import UsrModel

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class UsrSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UsrModel
        fields = ['email', 'age', 'name', 'lastName', 'country', 'gender', 'school', 'title', 'bio', 'created_at']
