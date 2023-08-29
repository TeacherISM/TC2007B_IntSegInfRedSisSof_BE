from django.contrib.auth.models import User, Group
from rest_framework import serializers
<<<<<<< Updated upstream
=======
from .models import Videogames
>>>>>>> Stashed changes

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
<<<<<<< Updated upstream
        fields = ['url', 'name']
=======
        fields = ['url', 'name']

class VideogamesSerializar(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Videogames
        fields = ['name', 'character', 'level']
>>>>>>> Stashed changes
