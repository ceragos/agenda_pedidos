from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Cliente(models.Model):
    nombre_completo = models.CharField(
        max_length=70
    )
    telefono = models.IntegerField(
        verbose_name='Teléfono'
    )
    direccion = models.CharField(
        max_length=70,
        verbose_name='dirección'
    )
    usuario = models.OneToOneField(
        User,
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='usuario_cliente'
    )

    class Meta:
        ordering = ['nombre_completo']

    def __str__(self) -> str:
        return self.nombre_completo
