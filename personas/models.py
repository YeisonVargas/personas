from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    foto = models.URLField(max_length=500)
    habilidad_uno = models.TextField()
    habilidad_dos = models.TextField()
    habilidad_tres = models.TextField()

    def __str__(self):
        return '{}'.format(self.nombre)