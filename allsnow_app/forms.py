from django import forms
from .models import SolicitudTienda
from .models import SolicitudUsuario

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
