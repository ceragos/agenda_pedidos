import requests
from datetime import datetime, timedelta
from django.db import models
from django.contrib.auth import get_user_model

from apps.agenda.models import Agenda

User = get_user_model()


class ConductorQuerySet(models.QuerySet):

    def disponibles(self, fecha_hora):
        fecha_hora_inicio = datetime.strptime(fecha_hora, "%Y-%m-%d %H:%M:%S")
        fecha_hora_fin = fecha_hora_inicio + timedelta(hours=1)

        agendamientos = Agenda.objects.filter(fecha_hora__gte=fecha_hora_inicio, fecha_hora__lte=fecha_hora_fin)
        return self.exclude(agenda_conductor__in=agendamientos)

    def cercano(self, fecha_hora, lat, lng):
        return self.disponibles(fecha_hora) \
            .extra(select={'distancia': f'SQRT(POWER({lat}-lat_ubicacion,2)+SQRT(POWER({lng}-lng_ubicacion,2)))'}) \
            .order_by('distancia')[:1]


class ConductorManager(models.Manager):

    def get_queryset(self):
        return ConductorQuerySet(self.model, using=self._db)

    def obtener_ubicacion(self):
        url = "https://gist.githubusercontent.com/jeithc/96681e4ac7e2b99cfe9a08ebc093787c/raw/632ca4fc3ffe77b558f467beee66f10470649bb4/points.json"

        response = requests.request("GET", url)

        for alfred in response.json()['alfreds']:
            conductor = self.get(id=alfred['id'])
            conductor.lat_ubicacion =  alfred['lat']
            conductor.lng_ubicacion = alfred['lng']
            conductor.save()


class Conductor(models.Model):
    nombre_completo = models.CharField(
        max_length=70
    )
    telefono = models.IntegerField()
    usuario = models.OneToOneField(
        User,
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='usuario_conductor'
    )
    lat_ubicacion = models.SmallIntegerField(
        default=0
    )
    lng_ubicacion = models.SmallIntegerField(
        default=0
    )

    objects = ConductorManager()

    class Meta:
        ordering = ['id']

    def __str__(self) -> str:
        return self.nombre_completo
