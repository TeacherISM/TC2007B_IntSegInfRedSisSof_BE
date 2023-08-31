from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import AlumnoModel

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=User
        #fields= ['url', 'username', 'email', 'groups']
        fields = '__all__'

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Group
        #field=['url', 'name']
        fields = '__all__'

class AlumnoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AlumnoModel
        fields = '__all__'