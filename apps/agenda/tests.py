from datetime import datetime
from rest_framework import status
from faker import Faker

from apps.core.tests import TestSetUp
from apps.conductores.models import Conductor
from apps.conductores.factories import ConductorFactory
from apps.clientes.factories import ClienteFactory
from apps.agenda.factories import AgendaFactory

faker = Faker()

class ConductorTestCase(TestSetUp):
    url = '/agenda/'

    def setUp(self):
        super().setUp()
        cliente_factory = ClienteFactory()
        cliente_factory.crear(self.user)
        ConductorFactory().registros_base()
        ClienteFactory().registros_base()
        AgendaFactory().registros_base()

    def test_reservar(self):
        conductor = Conductor.objects.first()
        response = self.client.post(
            self.url,
            {
                'conductor': conductor.id,
                'fecha': faker.date(),
                'hora': faker.time(),
                'lat_origen': faker.random_int(min=0, max=100),
                'lng_origen': faker.random_int(min=0, max=100),
                'destino': faker.address()
            },
            format='json'
        )
        print(conductor)
        print(response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_agenda_dia(self):
        fecha = datetime.strftime(datetime.now(), "%Y-%m-%d")
        response = self.client.get(
            self.url,
            {
                'fecha': fecha
            },
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_agenda_conductor(self):
        conductor = Conductor.objects.values('id').first()
        response = self.client.get(
            self.url,
            {
                'conductor': conductor['id']
            },
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
