from faker import Faker
from ddf import G
from django.db import transaction

from apps.agenda.models import Agenda

faker = Faker()


class AgendaFactory:

    def crear(self):
        agenda = G(Agenda)
        return agenda

    def registros_base(self):
        reservas = Agenda.objects.count()
        
        if not reservas:
            while True:
                try:
                    self.crear()
                    reservas = Agenda.objects.count()
                    print(f'Reserva #{reservas} creada')
                    if Agenda.objects.count() == 5:
                        break
                except:
                    print(f'Error creando reserva #{reservas + 1}')
