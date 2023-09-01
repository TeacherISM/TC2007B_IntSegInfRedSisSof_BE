from django.contrib.auth.models import User, Group
import SEL4C.app1.models as modelos
from django.contrib.auth.models import User, Group
from rest_framework import serializers


""" class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
 """

class AdminSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = modelos.Admin
        fields = ['username', 'correo', 'firstname', 'lastname']


class EmprendedorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = modelos.Emprendedor
        fields = ['username', 'correo', 'firstname','lastname', 'degree', 'institution', 'gender', 'age', 'country', 'studyField']


class ActividadSerializer():
    class Meta:
        model = modelos.Actividad
        fields = ['idActividad', 'numAct', 'idUsuario', 'title', 'description']


class ArchivoSerializer():
    class Meta:
        model = modelos.Archivo
        fields = ['idArchivo', 'idActividad', 'archivo', 'filetype']


class PreguntaSerializer():
    class Meta:
        model = modelos.Pregunta
        fields = ['idPregunta', 'idActividad', 'description']


class RespuestaSerializer():
    class Meta:
        model = modelos.Respuesta
        fields = ['idRespuesta','idPregunta', 'numero', 'texto']
