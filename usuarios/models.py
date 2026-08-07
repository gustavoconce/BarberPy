from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):
    TIPO_USUARIO = [
        ('CLIENTE', 'Cliente'),
        ('BARBEIRO', 'Barbeiro'),
        ('ADMIN', 'Administrador'),
    ]

    telefone = models.CharField(max_length=20, blank=True)

    tipo = models.CharField(
        max_length=20,
        choices=TIPO_USUARIO,
        default='CLIENTE'
    )

    foto = models.ImageField(
        upload_to='usuarios/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.get_full_name() or self.username