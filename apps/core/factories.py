from faker import Faker
from ddf import G
from django.contrib.auth import get_user_model
from django.db import transaction

faker = Faker()
User = get_user_model()

class UsuarioFactory:
    password = faker.password()

    def crear(self, password=None):
        if password:
            self.password = password
        with transaction.atomic():
            usuario = G(
                User,
                first_name=faker.first_name(),
                last_name=faker.last_name(),
                username=faker.first_name().lower()
            )
            usuario.set_password(self.password)
            usuario.save()
        return usuario
