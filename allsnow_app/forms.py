from django import forms
from .models import SolicitudTienda
from .models import SolicitudUsuario
from .models import Inventario
from .models import InventarioArriendo

class SolicitudTiendaForm(forms.ModelForm):
    class Meta:
        model = SolicitudTienda
        fields = ['nombre_tienda', 'patente_local', 'region']

class SolicitudUsuarioForm(forms.ModelForm):
    class Meta:
        model = SolicitudUsuario
        fields = ['nombre', 'apellido', 'rut', 'telefono', 'correo', 'conf_correo', 'contraseña', 'conf_contraseña']
        widgets = {
            'contraseña': forms.PasswordInput(),
            'conf_contraseña': forms.PasswordInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        correo = cleaned_data.get("correo")
        conf_correo = cleaned_data.get("conf_correo")
        contraseña = cleaned_data.get("contraseña")
        conf_contraseña = cleaned_data.get("conf_contraseña")

        if correo and conf_correo and correo != conf_correo:
            self.add_error('conf_correo', "Los correos deben coincidir.")

        if contraseña and conf_contraseña and contraseña != conf_contraseña:
            self.add_error('conf_contraseña', "Las contraseñas deben coincidir.")

        return cleaned_data

class InventarioForm(forms.ModelForm):
    class Meta:
        model = Inventario
        fields = ['nombre_producto', 'precio', 'cantidad_disponible', 'talla_producto']  # Cambia los campos según tu modelo
        labels = {
            'nombre_producto : nombre'
            'precio': 'Precio (CLP)', 
            'cantidad_disponible': 'Cantidad',
            'talla_producto': 'Talla',
        }
        widgets = {
            'precio': forms.NumberInput(attrs={
                'class': 'form-control', 
                'id': 'precio', 
                'step': '500',  
                'placeholder': 'Ingrese el precio en CLP'  
            }),
            'cantidad_disponible': forms.NumberInput(attrs={
                'class': 'form-control', 
                'id': 'cantidadDisponible'
            }),
            'talla_producto': forms.Select(attrs={'class': 'form-control', 'id': 'tallaProducto'}),  
        }

class InventarioArriendoForm(forms.ModelForm):
    class Meta:
        model = InventarioArriendo
        fields = ['nombre_producto', 'cantidad_disponible', 'talla_producto', 'precio_arriendo']
        labels = {
            'nombre_producto': 'Nombre',  
            'cantidad_disponible': 'Cantidad',
            'talla_producto': 'Talla',
            'precio_arriendo': 'Precio de Arriendo (CLP)',
        }
        widgets = {
            'precio_arriendo': forms.NumberInput(attrs={
                'class': 'form-control',
                'id': 'precioArriendo',
                'step': '500',  
                'placeholder': 'Ingrese el precio de arriendo en CLP'  
            }),
            'cantidad_disponible': forms.NumberInput(attrs={
                'class': 'form-control',
                'id': 'cantidadDisponible'
            }),
            'talla_producto': forms.Select(attrs={'class': 'form-control', 'id': 'talla_producto'}),
        }