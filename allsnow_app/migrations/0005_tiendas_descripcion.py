# Generated by Django 4.2.4 on 2024-11-05 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allsnow_app', '0004_inventario_nombre_producto_inventario_talla_producto_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tiendas',
            name='descripcion',
            field=models.TextField(blank=True, null=True),
        ),
    ]