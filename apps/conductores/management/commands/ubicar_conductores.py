from django.core.management.base import BaseCommand

from apps.conductores.tasks import obtener_ubicacion_conductores

class Command(BaseCommand):
    help = 'Registros base'

    def handle(self, *args, **options):
        obtener_ubicacion_conductores()
