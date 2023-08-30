from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import UsuarioModel

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UsuarioModel
        fields = ['user_email', 'user_fname', 'user_lname','user_level','user_school','user_gender','user_age','user_country','user_schooln','user_notes','created_at']