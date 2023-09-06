from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import HomeUser, Session, Survey, Deliver

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class HomeUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HomeUser
        fields = ['username', 'full_name' , 'pass_phase', 'email', 'created_at', 
                  'verified_at', 'last_login', 'time_spended', 'rol', 'birth', 'genre', 
                  'country', 'institution', 'carrer', 'grade']
        

class SessionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Session
        fields = ['user', 'ip_address', 'date_init', 'date_end']


class SurveySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Survey
        fields = ['user', 'date_init', 'date_end',                                                                          # Information
                  'question1', 'question2', 'question3', 'question4',                                                       # Autocontrol 
                  'question5', 'question6', 'question7', 'question8', 'question9', 'question10',                            # Leadership
                  'question11', 'question12', 'question13', 'question14', 'question15', 'question16', 'question17',         # Conscience and social value
                  'question18', 'question19', 'question20', 'question21', 'question22', 'question23', 'question24',         # Social innovation and financial sustainability
                  'question25', 'question26', 'question27', 'question28', 'question29', 'question30',                       # Systemic thinking
                  'question31', 'question32', 'question33', 'question34', 'question35', 'question36', 'question37',         # Scientific thinking
                  'question38', 'question39', 'question40', 'question41', 'question42', 'question43',                       # Critical thinking
                  'question44', 'question45', 'question46', 'question47', 'question48', 'question49']                       # Innovative thinking


class DeliverSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Deliver
        fields = ['user', 'date', 'text_file', 'image_file', 'url_file', 'file']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
        