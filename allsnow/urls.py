"""
URL configuration for allsnow project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from allsnow_app import views
from allsnow_app.views import agregar_productos_arriendo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('filtro_tienda/', views.filtro_tiendas, name='filtro_tienda'),
    path('administrador/', views.administrador, name='administrador'),
    path('inicio/', views.inicio, name='inicio'),
    path('inicio/trabaja-con-nosotros', views.trabaja_con_nosotros, name='trabaja_con_nosotros'),
    path('inicio/registrarme', views.registrarme, name='registrarme'),
    path('aprobar-solicitud/<int:solicitud_id>/', views.aprobar_solicitud, name='aprobar_solicitud'),
    path('rechazar-solicitud/<int:solicitud_id>/', views.rechazar_solicitud, name='rechazar_solicitud'),
    path('tienda/<int:id>/', views.tienda_detalle, name='tienda_detalle'),

    #### naty ######
    path('inventario_ventas/', views.inventario_ventas, name='inventario_ventas'),
    path('agregar_productos/', views.agregar_productos, name='agregar_productos'),
    path('editar_producto_arriendo/<int:id_producto>/', views.editar_producto_arriendo, name='editar_producto_arriendo'),
    path('inventario_arriendo/', views.inventario_arriendo, name='inventario_arriendo'),
    path('agregar_producto_arriendo/', agregar_productos_arriendo, name='agregar_productos_arriendo'),
    path('eliminar_producto_arriendo/<int:id_producto>/', views.eliminar_producto_arriendo, name='eliminar_producto_arriendo'),
    path('eliminar_productos/<int:id_producto>/', views.eliminar_productos, name='eliminar_productos'),
    path('editar_producto/', views.editar_producto, name='editar_producto'),
    path('interfaz_dueno/', views.interfaz_dueno, name='interfaz_dueno'),
    path('centro_rental_view/', views.centro_rental_view, name='centro_rental_view'),
    path('editar_descripcion_view/', views.editar_descripcion_view, name='editar_descripcion_view'),
]