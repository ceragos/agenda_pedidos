from rest_framework import status
from rest_framework.test import APITestCase

from django.test import TestCase, Client

from apps.core.factories import UsuarioFactory

class TestSetUp(APITestCase):

    def setUp(self):

        self.login_url = '/api/token/'
        usuario_factory = UsuarioFactory()
        self.user = usuario_factory.crear(usuario_factory.password)
        
        response = self.client.post(
            self.login_url,
            {
                'username': self.user.username,
                'password': usuario_factory.password
            },
            format='json'
        )
    
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.token = 'Bearer ' + response.json()['access']
        self.client.credentials(HTTP_AUTHORIZATION=self.token)
        return super().setUp()
