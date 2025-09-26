from django.urls import path
from . import views

urlpatterns = [
    path('agregar/', views.agregar_contacto, name='agregar_contacto'),
    path('', views.lista_contactos, name='lista_contactos'),
]