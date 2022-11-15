from django.db import models

from apps.clientes.models import Cliente


class Agenda(models.Model):
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.PROTECT,
        related_name='agenda_cliente'
    )
    conductor = models.ForeignKey(
        'conductores.Conductor',
        on_delete=models.PROTECT,
        related_name='agenda_conductor'
    )
    fecha = models.DateField(
        help_text='Fecha en la que se requiere agendar el servicio.'
    )
    hora = models.TimeField(
        help_text='Hora en la que se requiere agendar el servicio.'
    )
    fecha_hora = models.DateTimeField(
        blank=True,
        null=True,
        help_text='Fecha y hora en la que se requiere agendar el servicio.'
    )
    # Lugar de recogida
    lat_origen = models.SmallIntegerField()
    lng_origen = models.SmallIntegerField()
    # Lugar de destino
    destino = models.CharField(max_length=70)
    creado = models.DateTimeField(
        auto_now_add=True,
        help_text='Fecha y hora en que se crea el agendamiento del servicio.'
    )

    class Meta:
        ordering = ['fecha_hora']

    def __str__(self) -> str:
        return self.cliente.nombre_completo
