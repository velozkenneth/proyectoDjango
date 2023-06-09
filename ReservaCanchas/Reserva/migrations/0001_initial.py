# Generated by Django 4.1.7 on 2023-04-01 16:01

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cancha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=30)),
                ('costo_por_hora', models.FloatField(default=0)),
                ('esta_disponible', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora_inicio', models.DateTimeField(default=django.utils.timezone.now)),
                ('hora_fin', models.DateTimeField(default=django.utils.timezone.now)),
                ('cancha', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cancha', to='Reserva.cancha')),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('cedula', models.CharField(max_length=30)),
                ('correo', models.CharField(max_length=30)),
                ('telefono', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(default=django.utils.timezone.now)),
                ('esta_anulada', models.BooleanField(default=False)),
                ('horario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='horario', to='Reserva.horario')),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='persona', to='Reserva.persona')),
            ],
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(default=django.utils.timezone.now)),
                ('total', models.FloatField()),
                ('reserva', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='reserva', to='Reserva.reserva')),
            ],
        ),
    ]
