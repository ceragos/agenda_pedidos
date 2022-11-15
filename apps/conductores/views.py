from datetime import datetime, timedelta

from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from apps.conductores.models import Conductor
from apps.conductores.tasks import obtener_ubicacion_conductores
from apps.conductores.serializers import ConductorSerializer, ConductorDisponibleSerializer, ConductorCercanoSerializer


class ConductorViewSet(ModelViewSet):
    queryset=Conductor.objects.all()
    serializer_class = ConductorSerializer
    http_method_names = ['get']

    fecha_hora = openapi.Parameter('fecha_hora', openapi.IN_QUERY, description='Fecha y hora requerida', type=openapi.FORMAT_DATETIME)
    lat = openapi.Parameter('lat', openapi.IN_QUERY, description='Latitud cliente', type=openapi.TYPE_INTEGER)
    lng = openapi.Parameter('lng', openapi.IN_QUERY, description='Longitud cliente', type=openapi.TYPE_INTEGER)

    @swagger_auto_schema(manual_parameters=[fecha_hora])
    @action(detail=False, methods=['get'])
    def disponibles(self, request):
        serializer = ConductorDisponibleSerializer(data=request.GET)
        serializer.is_valid(raise_exception=True)

        fecha_hora = request.query_params.get('fecha_hora', None)
        queryset = self.queryset.disponibles(fecha_hora)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


    @swagger_auto_schema(manual_parameters=[fecha_hora, lat, lng])
    @action(detail=False, methods=['get'])
    def cercano(self, request):
        serializer = ConductorCercanoSerializer(data=request.GET)
        serializer.is_valid(raise_exception=True)

        fecha_hora = request.query_params.get('fecha_hora', None)
        lat = request.query_params.get('lat', None)
        lng = request.query_params.get('lng', None)
        
        queryset = self.queryset.cercano(fecha_hora, lat, lng)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def ubicar(self, request):
        obtener_ubicacion_conductores()
        return Response(status=status.HTTP_204_NO_CONTENT)
