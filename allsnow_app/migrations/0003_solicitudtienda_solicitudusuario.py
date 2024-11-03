# Generated by Django 3.1 on 2024-11-03 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allsnow_app', '0002_tiendas_region'),
    ]

    operations = [
        migrations.CreateModel(
            name='SolicitudTienda',
            fields=[
                ('id_solicitud_tienda', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_tienda', models.CharField(max_length=100)),
                ('patente_local', models.CharField(max_length=10)),
                ('region', models.CharField(choices=[('Arica y Parinacota', 'Arica y Parinacota'), ('Tarapacá', 'Tarapacá'), ('Antofagasta', 'Antofagasta'), ('Atacama', 'Atacama'), ('Coquimbo', 'Coquimbo'), ('Valparaíso', 'Valparaíso'), ('Metropolitana', 'Metropolitana'), ("O'Higgins", "O'Higgins"), ('Maule', 'Maule'), ('Ñuble', 'Ñuble'), ('Biobío', 'Biobío'), ('La Araucanía', 'La Araucanía'), ('Los Ríos', 'Los Ríos'), ('Los Lagos', 'Los Lagos'), ('Aysén', 'Aysén'), ('Magallanes', 'Magallanes')], default='Metropolitana de Santiago', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SolicitudUsuario',
            fields=[
                ('id_solicitud_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('rut', models.CharField(max_length=12)),
                ('telefono', models.IntegerField(max_length=9)),
                ('correo', models.EmailField(max_length=100)),
                ('conf_correo', models.EmailField(max_length=100)),
                ('contraseña', models.CharField(max_length=225)),
                ('conf_contraseña', models.CharField(max_length=225)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]