from django.db import models

# Create your models here.

class RolUsuario(models.Model):
    id_rol = models.AutoField(primary_key=True)
    rol = models.CharField(max_length=50)

    class Meta:
        db_table = 'Rol_Usuario'


class Usuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(max_length=100)
    contraseña = models.CharField(max_length=225)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Usuarios'


class Tiendas(models.Model):
    id_tienda = models.AutoField(primary_key=True)
    nombre_tienda = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=225)
    region = models.CharField(
    max_length=100,
    choices=[
        ("Arica y Parinacota", "Arica y Parinacota"),
        ("Tarapacá", "Tarapacá"),
        ("Antofagasta", "Antofagasta"),
        ("Atacama", "Atacama"),
        ("Coquimbo", "Coquimbo"),
        ("Valparaíso", "Valparaíso"),
        ("Metropolitana de Santiago", "Metropolitana de Santiago"),
        ("Libertador General Bernardo O'Higgins", "Libertador General Bernardo O'Higgins"),
        ("Maule", "Maule"),
        ("Ñuble", "Ñuble"),
        ("Biobío", "Biobío"),
        ("Araucanía", "Araucanía"),
        ("Los Ríos", "Los Ríos"),
        ("Los Lagos", "Los Lagos"),
        ("Aysén del General Carlos Ibáñez del Campo", "Aysén del General Carlos Ibáñez del Campo"),
        ("Magallanes y de la Antártica Chilena", "Magallanes y de la Antártica Chilena")
    ], default="Metropolitana de Santiago"
)
    estado_suscripcion = models.CharField(max_length=10, choices=[('activa', 'Activa'), ('desactiva', 'Desactiva')])
    class Meta:
        db_table = 'Tiendas'


class UsuarioTienda(models.Model):
    id_usuario_tienda = models.AutoField(primary_key=True)
    id_tienda = models.ForeignKey(Tiendas, on_delete=models.CASCADE)
    id_rol = models.ForeignKey(RolUsuario, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Usuario_Tienda'


class Ventas(models.Model):
    id_venta = models.AutoField(primary_key=True)
    fecha_venta = models.DateTimeField(auto_now_add=True)
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
    id_usuario_tienda = models.ForeignKey(UsuarioTienda, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Ventas'


class Inventario(models.Model):
    id_producto = models.AutoField(primary_key=True)
    id_tienda = models.ForeignKey(Tiendas, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad_disponible = models.IntegerField()

    class Meta:
        db_table = 'Inventario'


class Productos(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=100)
    descripcion = models.TextField()
    tipo = models.CharField(max_length=10, choices=[('arriendo', 'Arriendo'), ('venta', 'Venta')])

    class Meta:
        db_table = 'Productos'


class Arriendos(models.Model):
    id_arriendo = models.AutoField(primary_key=True)
    fecha_arriendo = models.DateTimeField(auto_now_add=True)
    fecha_devolucion = models.DateTimeField(null=True, blank=True)
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
    id_usuario_tienda = models.ForeignKey(UsuarioTienda, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Arriendos'


class DetalleArriendo(models.Model):
    id_detallea = models.AutoField(primary_key=True)
    id_arriendo = models.ForeignKey(Arriendos, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Inventario, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'Detalle_Arriendo'


class DetallesVenta(models.Model):
    id_detallev = models.AutoField(primary_key=True)
    id_venta = models.ForeignKey(Ventas, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Inventario, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'Detalles_Venta'


class Suscripcion(models.Model):
    id_sub = models.AutoField(primary_key=True)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    id_tienda = models.ForeignKey(Tiendas, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Suscripcion'
