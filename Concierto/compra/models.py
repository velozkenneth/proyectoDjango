from django.db import models
from django.utils.timezone import now
# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    cedula = models.CharField(max_length=30)
    telefono = models.CharField(max_length=30)
    user = models.OneToOneField('auth.user', on_delete=models.PROTECT, related_name='user', default=None)

    def __str__(self) -> str:
        return f"{self.nombre}"

class Concierto(models.Model):
    titulo = models.CharField(max_length=100)
    artista = models.CharField(max_length=30)
    poster = models.ImageField(verbose_name="Poster", upload_to="./static/compra/")
    descripcion = models.CharField(max_length=200)
    fecha = models.DateTimeField(default=now)
    precio_ticket = models.FloatField()
    capacidad = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f"{self.titulo}  :  {self.artista}"

class Ubicacion(models.Model):
    ciudad = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.ciudad}"

class Ticket(models.Model):
    codigo = models.IntegerField()
    compra = models.ForeignKey("Compra",on_delete=models.CASCADE)

class Compra(models.Model):
    persona = models.ForeignKey('Persona', on_delete=models.PROTECT)
    ubicacion = models.ForeignKey('Ubicacion', on_delete=models.PROTECT)
    concierto = models.ForeignKey('Concierto', on_delete=models.PROTECT)
    fecha_compra = models.DateTimeField(default=now)
    num_tickets = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f"{self.concierto}"

class CompraStatus(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.PROTECT, related_name="compra")
    status = models.BooleanField(verbose_name="Status", default=True) #Por defecto todo correcto
    total = models.DecimalField(verbose_name="Total",max_digits=6, decimal_places=2)

