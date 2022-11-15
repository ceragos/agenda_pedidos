# Generated by Django 3.2.16 on 2022-11-13 15:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_completo', models.CharField(max_length=70)),
                ('telefono', models.IntegerField(verbose_name='Teléfono')),
                ('direccion', models.CharField(max_length=70, verbose_name='dirección')),
                ('usuario', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='usuario_cliente', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['nombre_completo'],
            },
        ),
    ]