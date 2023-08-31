from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from app1.serializers import UserSerializer, GroupSerializer, AlumnoSerializer
from app1.models import AlumnoModel

# Create your views here.

"""
En una vista basada en conjuntos de DRF, como ModelViewSet, la conexión entre queryset y serializer_class se establece mediante el comportamiento predeterminado de DRF. Cuando se realiza una solicitud HTTP a una URL que coincide con una vista basada en conjuntos, como UserViewSet, DRF maneja el proceso de recuperar los datos y serializarlos automáticamente.

Aquí está cómo funciona la conexión:

Recuperación de Datos (queryset): Cuando se accede a una URL que corresponde a la vista UserViewSet, DRF toma el queryset definido en la vista (queryset = User.objects.all().order_by('-date_joined')) y lo ejecuta en la base de datos. Esto recupera todos los objetos User de la base de datos y los almacena en una lista.

Serialización de Datos (serializer_class): Luego, DRF utiliza el serializer_class definido en la vista (serializer_class = UserSerializer) para serializar la lista de objetos User recuperados. El serializador toma cada objeto User, aplica la lógica definida en UserSerializer para convertirlo en un formato legible (como JSON) y agrega estos objetos serializados a una lista.

Respuesta JSON: Finalmente, DRF toma la lista de objetos serializados y la convierte en una respuesta HTTP con formato JSON. Esta respuesta JSON se envía al cliente que realizó la solicitud.

En resumen, aunque no hay una línea de código que conecte directamente queryset y serializer_class, el flujo interno de Django REST Framework los conecta de manera automática y se encarga de la recuperación de datos y la serialización de datos basándose en la configuración que has proporcionado en la vista y el serializador.
"""
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class AlumnoViewSet(viewsets.ModelViewSet):
    queryset = AlumnoModel.objects.all()
    serializer_class = AlumnoSerializer
    permissions_classes = [permissions.IsAuthenticated]

"""
Una vista basada en conjuntos (también conocida como ViewSet) en Django REST Framework (DRF) es una vista que proporciona automáticamente una serie de acciones CRUD (Crear, Leer, Actualizar, Eliminar) para un modelo específico. Esta vista es muy útil para simplificar la creación de APIs RESTful que manejan operaciones en conjuntos de objetos de un modelo.

En DRF, hay varios tipos de vistas basadas en conjuntos:

ModelViewSet: Proporciona todas las acciones CRUD (listar, crear, recuperar, actualizar, eliminar) para un modelo.

ReadOnlyModelViewSet: Proporciona solo acciones de lectura (listar y recuperar) para un modelo.

ModelViewSet personalizado: Puedes personalizar las acciones que se proporcionan y cómo funcionan.

Cuando defines una vista basada en conjuntos (ViewSets), estás estableciendo una conexión entre el modelo, el serializador y las acciones CRUD. El ViewSet maneja automáticamente la lógica de la API y la relación entre el modelo y el serializador.
"""