from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

from .models import UsuarioModel

class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UsuarioModel
        fields = ['nombre', 'contraseña', 'edad', 'genero', 'puntF', 'puntI', 'created_at']