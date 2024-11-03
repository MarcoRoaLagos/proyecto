# views.py
from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from .models import Tiendas, SolicitudTienda,Suscripcion

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
    solicitudes = SolicitudTienda.objects.all()  # Obtener todas las solicitudes de tienda
    tiendas = Tiendas.objects.all()              # Obtener todas las tiendas
    suscripciones = Suscripcion.objects.all()    # Obtener todas las suscripciones

    context = {
        'solicitudes': solicitudes,
        'tiendas': tiendas,
        'suscripciones': suscripciones
    }
    
    return render(request, 'administrador.html', context)

def aprobar_solicitud(request, solicitud_id):
    # Obtiene la solicitud de tienda usando el campo correcto 'id_solicitud_tienda'
    solicitud = get_object_or_404(SolicitudTienda, id_solicitud_tienda=solicitud_id)
    
    # Crea una nueva entrada en Tiendas usando los datos de la solicitud
    Tiendas.objects.create(
        nombre=solicitud.nombre_tienda,
        # Asigna otros campos necesarios de la solicitud, como se definen en tu modelo Tiendas
        # por ejemplo: patente_local=solicitud.patente_local, region=solicitud.region
    )
    
    # Elimina la solicitud de tienda después de aprobarla
    solicitud.delete()
    return redirect(reverse('administrador'))

def rechazar_solicitud(request, solicitud_id):
    # Obtiene la solicitud de tienda usando el campo correcto 'id_solicitud_tienda'
    solicitud = get_object_or_404(SolicitudTienda, id_solicitud_tienda=solicitud_id)
    
    # Elimina la solicitud de tienda al rechazarla
    solicitud.delete()
    return redirect(reverse('administrador'))

def inicio(request):
    return render(request, 'inicio.html')

def trabaja_con_nosotros(request):
    return render(request, 'inicio.html')

def registrarme(request):
    return render(request, 'inicio.html')