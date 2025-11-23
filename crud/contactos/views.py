from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from .forms import ContactoForm
from .models import Contactos
from django.contrib.auth.decorators import login_required

from rest_framework import permissions, viewsets
from django.contrib.auth.models import Group, User
from .serializers import ContactosSerializer, UserSerializer, GroupSerializer


class ContactosViewSet(viewsets.ModelViewSet):
    queryset = Contactos.objects.all().order_by("nombre")
    serializer_class = ContactosSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all().order_by("name")
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


# Etiqueta model and viewset removed per request

def lista_contactos(request):
    query = request.GET.get('q', '')
    if query:
        contactos_list = Contactos.objects.filter(
            Q(nombre__icontains=query) |
            Q(correo__icontains=query)
        )
    else:
        contactos_list = Contactos.objects.all()
    
    paginator = Paginator(contactos_list, 10)  # 10 contactos por página
    page = request.GET.get('page')
    contactos = paginator.get_page(page)
    
    return render(request, 'contactos/lista_contactos.html', {
        'contactos': contactos,
        'query': query
    })

def crear_contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Contacto creado exitosamente.')
                return redirect('lista_contactos')
            except Exception as e:
                messages.error(request, f'Error al crear el contacto: {str(e)}')
        else:
            messages.error(request, 'Por favor corrija los errores en el formulario.')
    else:
        form = ContactoForm()
    
    return render(request, 'contactos/formulario_contacto.html', {
        'form': form,
        'titulo': 'Crear Contacto'
    })

def editar_contacto(request, pk):
    contacto = get_object_or_404(Contactos, pk=pk)
    if request.method == 'POST':
        form = ContactoForm(request.POST, instance=contacto)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Contacto actualizado exitosamente.')
                return redirect('lista_contactos')
            except Exception as e:
                messages.error(request, f'Error al actualizar el contacto: {str(e)}')
        else:
            messages.error(request, 'Por favor corrija los errores en el formulario.')
    else:
        form = ContactoForm(instance=contacto)
    
    return render(request, 'contactos/formulario_contacto.html', {
        'form': form,
        'titulo': 'Editar Contacto'
    })

def eliminar_contacto(request, pk):
    contacto = get_object_or_404(Contactos, pk=pk)
    try:
        contacto.delete()
        messages.success(request, 'Contacto eliminado exitosamente.')
    except Exception as e:
        messages.error(request, f'Error al eliminar el contacto: {str(e)}')
    return redirect('lista_contactos')
