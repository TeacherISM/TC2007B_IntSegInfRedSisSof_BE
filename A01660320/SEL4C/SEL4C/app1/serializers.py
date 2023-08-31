from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import directorio

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class directorioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = directorio
        fields = ['nombre', 'apellidos', 'pais', 'sexo', 'telefono', 'correo', 'direccion']