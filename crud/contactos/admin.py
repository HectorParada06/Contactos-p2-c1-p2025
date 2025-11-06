from django.contrib import admin
from django.http import HttpResponse
import csv
from .models import Contactos

@admin.register(Contactos)
class ContactosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'correo', 'telefono')
    search_fields = ('nombre', 'correo')
    actions = ['exportar_como_csv']

    def exportar_como_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="contactos.csv"'
        
        writer = csv.writer(response)
        # Escribir encabezados
        writer.writerow(['Nombre', 'Correo', 'Teléfono', 'Dirección'])
        
        # Escribir datos
        for contacto in queryset:
            writer.writerow([
                contacto.nombre,
                contacto.correo,
                contacto.telefono,
                contacto.direccion
            ])
        
        return response
    
    exportar_como_csv.short_description = "Exportar seleccionados a CSV"