from datetime import datetime
from rest_framework import status
from faker import Faker

from apps.core.tests import TestSetUp
from apps.conductores.models import Conductor
from apps.conductores.factories import ConductorFactory
from apps.clientes.factories import ClienteFactory

faker = Faker()

class ConductorTestCase(TestSetUp):
    url = '/conductores/'

    def setUp(self):
        super().setUp()
        ConductorFactory().registros_base()

    def test_conductores_disponibles(self):
        fecha_hora = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")
        response = self.client.get(
            self.url + 'disponibles/',
            {
                'fecha_hora': fecha_hora
            },
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Conductor.objects.all().disponibles(fecha_hora).count(), response.json()['count'])


    def test_conductor_cercano(self):
        fecha_hora = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")
        lat = faker.random_int(min=0, max=100)
        lng = faker.random_int(min=0, max=100)
        response = self.client.get(
            self.url + 'cercano/',
            {
                'fecha_hora': fecha_hora,
                'lat': lat,
                'lng': lng
            },
            format='json'
        )
        conductor_obj = Conductor.objects.values('id').all().cercano(fecha_hora, lat, lng).first()
        conductor_res = response.json()['results'][0]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(conductor_obj['id'], conductor_res['id'])
