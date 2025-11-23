import re
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

class Contactos(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(
        max_length=20,
        validators=[
            RegexValidator(
                regex=r'^\+?\d{10,15}$',
                message='El teléfono debe contener solo números y tener entre 10 y 15 dígitos. Puede iniciar con +.',
                code='invalid_telefono'
            )
        ],
        help_text='Número con 10-15 dígitos, puede incluir +'
    )
    correo = models.EmailField()
    direccion = models.CharField(max_length=255)

    def clean(self):
        if not re.match(r'^\+?\d{10,15}$', self.telefono):
            raise ValidationError({'telefono': 'El teléfono debe contener solo números y tener entre 10 y 15 dígitos.'})

    def __str__(self):
        return self.nombre