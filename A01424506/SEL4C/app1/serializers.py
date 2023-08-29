from django.contrib.auth.models import User, Group
from rest_framework import serializers

#Librería para segundo ejercicio de Django, clase semana 3.
from .models import HomeModel

class HomeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HomeModel
        fields = ['title', 'content', 'created_at']


#Parte de código de la primera práctica de Django, clase semana 2.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']



class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']