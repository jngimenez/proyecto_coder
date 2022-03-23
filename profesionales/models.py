from django.db import models

# Create your models here.
class cerrajero(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    desempleado = models.BooleanField()

class futbolista(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    club_futbol = models.CharField(max_length=40)

class estudiante(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    institucion = models.CharField(max_length=40)
