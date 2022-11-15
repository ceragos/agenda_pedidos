from faker import Faker
from ddf import G
from django.db import transaction

from apps.clientes.models import Cliente
from apps.core.factories import UsuarioFactory

faker = Faker()


class ClienteFactory:

    def crear(self, usuario=None):
        usuario = usuario or UsuarioFactory().crear()
        cliente = G(Cliente, nombre_completo=f'{usuario.first_name} {usuario.last_name}', usuario=usuario)
        return cliente

    def registros_base(self):
        clientes = Cliente.objects.count()
        
        if not clientes:
            while True:
                try:
                    self.crear()
                    clientes = Cliente.objects.count()
                    print(f'Cliente #{clientes} creado')
                    if clientes == 2:
                        break
                except:
                    print(f'Error creando cliente #{clientes + 1}')
