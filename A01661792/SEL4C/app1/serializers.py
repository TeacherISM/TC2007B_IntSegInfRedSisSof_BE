from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Clientes, AguasFrescas, Ventas




class ClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clientes
        fields = ['numero_de_cliente'] 

class AguasFrescasSerializer(serializers.ModelSerializer):
    class Meta:
        model = AguasFrescas
        fields = ['nombre_agua', 'litros', 'created_at']  

class VentaSerializer(serializers.ModelSerializer):
    cliente = ClientesSerializer()
    agua_fresca = AguasFrescasSerializer()

    class Meta:
        model = Ventas
        fields = ['cliente', 'agua_fresca', 'fecha_venta']  

