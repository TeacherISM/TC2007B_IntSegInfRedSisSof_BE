from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import HomeUser

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class HomeUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HomeUser
        fields = ['username', 'full_name' , 'email', 'created_at', 
                  'last_login', 'time_spended', 'rol', 'birth', 'genre', 
                  'country', 'institution', 'carrer', 'grade']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
        