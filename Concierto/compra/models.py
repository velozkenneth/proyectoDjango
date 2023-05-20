from django.db import models
from django.utils.timezone import now
# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    cedula = models.CharField(max_length=30)
    correo = models.CharField(max_length=30)
    telefono = models.CharField(max_length=30)

class Concierto(models.Model):
    titulo = models.CharField(max_length=100)
    artista = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=200)
    fecha = models.DateTimeField(default=now)
    precio = models.FloatField()

class Ubicacion(models.Model):
     ciudad = models.CharField(max_length=20)
     direccion = models.CharField(max_length=50)
     capacidad = models.PositiveIntegerField()

class Compra(models.Model):
    persona = models.ForeignKey('Persona', on_delete=models.PROTECT)
    ubicacion = models.ForeignKey('Ubicacion', on_delete=models.PROTECT)
    concierto = models.ForeignKey('Concierto', on_delete=models.PROTECT, related_name="concierto")
    fecha = models.DateTimeField(default=now)
    num_tickets = models.PositiveIntegerField()
    cancelada = models.BooleanField(default=False)