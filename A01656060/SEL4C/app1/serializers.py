from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import ActivityModel, AdvanceModel, RetroModel

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url','username','email','groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ActivityModel
        fields = ['id', 'name', 'question', 'done']

class AdvanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AdvanceModel
        fields = ['id', 'advanceNum']

class RetroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RetroModel
        fields = ['id', 'retroFromAdmin']