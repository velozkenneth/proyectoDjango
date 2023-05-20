from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Persona(models.Model):
    user = models.OneToOneField('auth.user', on_delete=models.PROTECT , related_name='user', default=None)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    cedula = models.CharField(max_length=30)
    #correo = models.CharField(max_length=30)
    telefono = models.CharField(max_length=30)
    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}"

class Cancha(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=30)
    costo_por_hora = models.FloatField(default=0)
    esta_disponible = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.nombre}"

class Horario(models.Model):
    hora_inicio = models.DateTimeField(default=timezone.now)
    hora_fin = models.DateTimeField(default=timezone.now)
    cancha = models.ForeignKey('Cancha',on_delete=models.PROTECT, related_name='cancha')

class Reserva(models.Model):
    fecha_creacion = models.DateTimeField(default=timezone.now)
    persona = models.ForeignKey('Persona',on_delete=models.PROTECT, related_name='persona')
    horario = models.ForeignKey('Horario',on_delete=models.PROTECT, related_name='horario')
    esta_anulada = models.BooleanField(default=False)

class Pago(models.Model):
    fecha_creacion = models.DateTimeField(default=timezone.now)
    reserva = models.ForeignKey('Reserva', on_delete=models.PROTECT, related_name='reserva')
    total = models.FloatField()