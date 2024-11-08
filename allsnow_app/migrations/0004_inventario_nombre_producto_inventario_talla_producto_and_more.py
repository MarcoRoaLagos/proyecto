# Generated by Django 4.2.16 on 2024-11-04 01:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('allsnow_app', '0003_solicitudtienda_solicitudusuario_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventario',
            name='nombre_producto',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='inventario',
            name='talla_producto',
            field=models.CharField(choices=[('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL'), ('35', '35'), ('36', '36'), ('37', '37'), ('38', '38'), ('39', '39'), ('40', '40'), ('41', '41'), ('42', '42'), ('43', '43'), ('44', '44'), ('45', '45')], default='45', max_length=10),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='id_tienda',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='allsnow_app.tiendas'),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='precio',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='solicitudtienda',
            name='region',
            field=models.CharField(choices=[('Arica y Parinacota', 'Arica y Parinacota'), ('Tarapacá', 'Tarapacá'), ('Antofagasta', 'Antofagasta'), ('Atacama', 'Atacama'), ('Coquimbo', 'Coquimbo'), ('Valparaíso', 'Valparaíso'), ('Metropolitana', 'Metropolitana'), ("O'Higgins", "O'Higgins"), ('Maule', 'Maule'), ('Ñuble', 'Ñuble'), ('Biobío', 'Biobío'), ('La Araucanía', 'La Araucanía'), ('Los Ríos', 'Los Ríos'), ('Los Lagos', 'Los Lagos'), ('Aysén', 'Aysén'), ('Magallanes', 'Magallanes')], max_length=100),
        ),
        migrations.AlterField(
            model_name='solicitudusuario',
            name='telefono',
            field=models.IntegerField(),
        ),
        migrations.AlterModelTable(
            name='solicitudtienda',
            table='Solicitud_Tienda',
        ),
        migrations.CreateModel(
            name='InventarioArriendo',
            fields=[
                ('id_producto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_producto', models.CharField(blank=True, max_length=25, null=True)),
                ('precio_arriendo', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('cantidad_disponible', models.IntegerField()),
                ('talla_producto', models.CharField(choices=[('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL'), ('35', '35'), ('36', '36'), ('37', '37'), ('38', '38'), ('39', '39'), ('40', '40'), ('41', '41'), ('42', '42'), ('43', '43'), ('44', '44'), ('45', '45')], default='45', max_length=10)),
                ('id_tienda', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='allsnow_app.tiendas')),
            ],
            options={
                'db_table': 'InventarioArriendo',
            },
        ),
        migrations.AlterField(
            model_name='detallearriendo',
            name='id_producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='allsnow_app.inventarioarriendo'),
        ),
    ]
