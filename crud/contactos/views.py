from django.shortcuts import render, redirect
from .forms import AgregarContactoForm
from .models import Contactos
from django.db.models import Q

def agregar_contacto(request):
    if request.method == 'POST':
        form = AgregarContactoForm(request.POST)
        if form.is_valid():
            Contactos.objects.create(
                nombre=form.cleaned_data['nombre'],
                telefono=form.cleaned_data['telefono'],
                correo=form.cleaned_data['correo'],
                direccion=form.cleaned_data['direccion']
            )
            return redirect('lista_contactos')
    else:
        form = AgregarContactoForm()
    return render(request, 'contactos/agregar_contacto.html', {'form': form})

def lista_contactos(request):
    query = request.GET.get('q', '')
    if query:
        contactos = Contactos.objects.filter(
            Q(nombre__icontains=query) | Q(correo__icontains=query)
        )
    else:
        contactos = Contactos.objects.all()
    return render(request, 'contactos/lista_contactos.html', {'contactos': contactos})
