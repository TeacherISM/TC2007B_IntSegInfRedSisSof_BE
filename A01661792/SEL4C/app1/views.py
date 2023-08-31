from django.contrib.auth.models import User, Group
from rest_framework import permissions, viewsets
from django.http import JsonResponse
from django.shortcuts import render
from .models import Clientes, Ventas, AguasFrescas 
from .serializers import ClientesSerializer, VentaSerializer, AguasFrescasSerializer



def home(request):
    return JsonResponse({'message': 'Hello World'})



class AguasFrescasViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows AguasFrescas to be viewed or edited.
    """
    queryset = AguasFrescas.objects.all()
    serializer_class = AguasFrescasSerializer
    permission_classes = [permissions.IsAuthenticated]

class VentaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Venta to be viewed or edited.
    """
    queryset = Ventas.objects.all()
    serializer_class = VentaSerializer
    permission_classes = [permissions.IsAuthenticated]

class ClientesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Clientes to be viewed or edited.
    """
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializer
    permission_classes = [permissions.IsAuthenticated]
