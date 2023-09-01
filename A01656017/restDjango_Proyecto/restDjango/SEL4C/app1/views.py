from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
import SEL4C.app1.models as models
import SEL4C.app1.serializers as serializers


""" class UserViewSet(viewsets.ModelViewSet):
    
    API endpoint that allows users to be viewed or edited.
    
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = serializers.UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
 
    API endpoint that allows groups to be viewed or edited.

    permission_classes = [permissions.IsAuthenticated]
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer
 """

class AdminViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Usuarios to be viewed or edited.
    """
    permission_classes = [permissions.IsAuthenticated]
    queryset = models.Admin.objects.all()
    serializer_class = serializers.AdminSerializer


class EmprendedorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Usuarios to be viewed or edited.
    """
    permission_classes = [permissions.IsAuthenticated]
    queryset = models.Emprendedor.objects.all()
    serializer_class = serializers.EmprendedorSerializer


class ActividadViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Actividades to be viewed or edited.
    """
    permission_classes = [permissions.IsAuthenticated]
    queryset = models.Actividad.objects.all()
    serializer_class = serializers.ActividadSerializer


class ArchivoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Archivos to be viewed or edited.
    """
    permission_classes = [permissions.IsAuthenticated]
    queryset = models.Archivo.objects.all()
    serializer_class = serializers.ArchivoSerializer


class PreguntaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Preguntas to be viewed or edited.
    """
    permission_classes = [permissions.IsAuthenticated]
    queryset = models.Pregunta.objects.all()
    serializer_class = serializers.PreguntaSerializer


class RespuestaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Respuestas to be viewed or edited.
    """
    permission_classes = [permissions.IsAuthenticated]
    queryset = models.Respuesta.objects.all()
    serializer_class = serializers.RespuestaSerializer