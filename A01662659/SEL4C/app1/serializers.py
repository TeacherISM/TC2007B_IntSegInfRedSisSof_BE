from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import StudentModel

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StudentModel
        fields = ['first_name', 'last_name', 'gender', 'age', 'edu_lvl']