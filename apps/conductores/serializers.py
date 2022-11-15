from rest_framework import serializers

from .models import Conductor


class ConductorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Conductor
        fields = ['id', 'nombre_completo', 'telefono']


class ConductorDisponibleSerializer(serializers.Serializer):
    fecha_hora = serializers.DateTimeField()


class ConductorCercanoSerializer(ConductorDisponibleSerializer):
    lat = serializers.IntegerField(min_value=0, max_value=100)
    lng = serializers.IntegerField(min_value=0, max_value=100)
