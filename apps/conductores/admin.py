from django.contrib import admin
from apps.conductores.models import Conductor


@admin.register(Conductor)
class ConductorAdmin(admin.ModelAdmin):
    list_display = [
        'nombre_completo',
        'usuario',
        'telefono',
        'lat_ubicacion',
        'lng_ubicacion',
    ]
    readonly_fields = ['usuario']
