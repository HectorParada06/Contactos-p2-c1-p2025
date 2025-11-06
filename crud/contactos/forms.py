from django import forms
import re
from .models import Contactos

class ContactoForm(forms.ModelForm):
    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono', '')
        if not re.match(r'^\+?\d{10,15}$', telefono):
            raise forms.ValidationError('Ingrese un número válido (10-15 dígitos, puede incluir +).')
        return telefono
    class Meta:
        model = Contactos
        fields = ['nombre', 'telefono', 'correo', 'direccion']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
                'pattern': '^\+?\d{10,15}$',
                'title': 'Ingrese un número válido (10-15 dígitos, puede incluir +)'
            }),
            'correo': forms.EmailInput(attrs={
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'direccion': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'
            })
        }