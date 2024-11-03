# views.py
from django.shortcuts import render
from .models import Tiendas, Inventario

from django.shortcuts import render
from .models import Tiendas

def filtro_tiendas(request):
    # Filtra solo las tiendas con suscripción activa
    tiendas = Tiendas.objects.filter(estado_suscripcion='activa')  # Cambia 'activa' por el valor correspondiente si es diferente

    # Obtener los filtros
    region = request.GET.get('region')
    nombre_tienda = request.GET.get('nombre')

    # Verificar si hay filtros aplicados
    if region and region != "Seleccionar región":
        tiendas = tiendas.filter(region=region)

    if nombre_tienda:
        tiendas = tiendas.filter(nombre_tienda__icontains=nombre_tienda)

    # Si no se aplicó ningún filtro, no mostrar resultados
    if not region and not nombre_tienda:
        tiendas = Tiendas.objects.none()  # No devolver tiendas si no hay filtros

    # Obtener opciones de regiones
    regiones = Tiendas._meta.get_field('region').choices

    context = {
        'tiendas': tiendas,
        'selected_region': region,
        'regiones': regiones  # Agregar las opciones de región al contexto
    }
    return render(request, 'filtro_tienda.html', context)


def administrador(request):
    return render(request,'administrador.html')

def inicio(request):
    return render(request, 'inicio.html')

def trabaja_con_nosotros(request):
    return render(request, 'inicio.html')

def registrarme(request):
    return render(request, 'inicio.html')