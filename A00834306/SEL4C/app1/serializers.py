from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import usuario

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class usuariosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = usuario
        fields = ['nombre','apellido','edad']