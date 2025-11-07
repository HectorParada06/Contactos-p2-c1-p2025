from django.urls import path
from . import views
from django.urls import include, path
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"groups", views.GroupViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path('', views.lista_contactos, name='lista_contactos'),
    path('crear/', views.crear_contacto, name='crear_contacto'),
    path('editar/<int:pk>/', views.editar_contacto, name='editar_contacto'),
    path('eliminar/<int:pk>/', views.eliminar_contacto, name='eliminar_contacto'),
]