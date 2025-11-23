from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import Contactos


class ContactosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contactos
        fields = [
            "url",
            "id",
            "nombre",
            "telefono",
            "correo",
            "direccion",
        ]


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            "url",
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "is_staff",
        ]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "id", "name"]

