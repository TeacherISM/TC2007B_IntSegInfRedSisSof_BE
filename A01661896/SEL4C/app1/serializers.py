from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import PCMaster

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url','username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class PCMasterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PCMaster
        fields = ['id','procesador', 'tarjetaGrafica','NumVentiladores', 'FuentePoder', 'FechaConsulta']
        