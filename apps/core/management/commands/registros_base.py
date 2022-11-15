from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from faker import Faker

from apps.clientes.factories import ClienteFactory
from apps.conductores.models import Conductor
from apps.conductores.factories import ConductorFactory
from apps.core.providers import EmailProvider

User = get_user_model()

fake = Faker()
fake.add_provider(EmailProvider)

class Command(BaseCommand):
    help = 'Registros base'

    def handle(self, *args, **options):
        
        ConductorFactory().registros_base()

        ClienteFactory().registros_base()

        usuario = User(
            username='ceragos',
            email=fake.custom_email(),
            first_name=fake.name(),
            last_name=fake.last_name(),
            is_staff=True,
            is_superuser=True
        )
        usuario.set_password('seforabu-7')
        usuario.save()
