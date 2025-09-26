from django import forms

class AgregarContactoForm(forms.Form):
    nombre = forms.CharField(max_length=100, label="Nombre")
    telefono = forms.CharField(max_length=20, label="Teléfono")
    correo = forms.EmailField(label="Correo")  # EmailField valida el formato automáticamente
    direccion = forms.CharField(max_length=255, label="Dirección")