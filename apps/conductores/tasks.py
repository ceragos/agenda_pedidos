import logging
from celery import shared_task

from apps.conductores.models import Conductor

logger = logging.getLogger('CORE')

@shared_task()
def obtener_ubicacion_conductores():
    logger.info('Actualizando ubicación de los conductores...')
    Conductor.objects.obtener_ubicacion()
