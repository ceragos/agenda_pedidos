from faker import Faker
from ddf import G
from django.db import transaction

from apps.conductores.models import Conductor
from apps.core.factories import UsuarioFactory

faker = Faker()


class ConductorFactory:

    def crear(self, usuario=None):
        usuario = usuario or UsuarioFactory().crear()
        with transaction.atomic():
            conductor = G(
                Conductor,
                nombre_completo=f'{usuario.first_name} {usuario.last_name}',
                usuario=usuario,
                lat_ubicacion=faker.random_int(min=0, max=100),
                lng_ubicacion=faker.random_int(min=0, max=100)
            )
        return conductor

    def registros_base(self):
        conductores = Conductor.objects.count()
        
        if not conductores:
            while True:
                try:
                    self.crear()
                    conductores = Conductor.objects.count()
                    print(f'Conductor #{conductores} creado')
                    if Conductor.objects.count() == 20:
                        break
                except:
                    print(f'Error creando conductor #{conductores + 1}')
