from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Carro

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class CarroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Carro
        fields = ['marca','modelo','color','anio']
