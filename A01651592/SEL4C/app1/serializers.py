from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import AlumnoModel

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=User
        fields= ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Group
        field=['url', 'name']

class AlumnoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AlumnoModel
        fields = {'nombre', 'apellido', 'fecha_nacimiento', 'direccion', 'correo_electronico', 'telefono', 'fecha_inscripcion'}