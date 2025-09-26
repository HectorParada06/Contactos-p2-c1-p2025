from django.db import models

class Contactos(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField()
    direccion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre