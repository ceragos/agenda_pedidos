from django.contrib import admin
from apps.agenda.models import Agenda


@admin.register(Agenda)
class AgendaAdmin(admin.ModelAdmin):
    list_display = [
        'cliente',
        'conductor',
        'fecha',
        'hora',
        'lat_origen',
        'lng_origen',
        'destino',
        'creado',
    ]
    readonly_fields = ['cliente', 'conductor', 'creado',]
    fields = list_display
