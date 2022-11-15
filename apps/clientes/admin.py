from django.contrib import admin

from apps.clientes.models import Cliente


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = [
        'nombre_completo',
        'telefono',
        'direccion'
    ]
    readonly_fields = ['usuario']
