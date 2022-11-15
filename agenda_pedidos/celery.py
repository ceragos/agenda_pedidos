import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "agenda_pedidos.settings.docker")
app = Celery("agenda_pedidos")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
