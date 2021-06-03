from django.db import models
from django.db.models import fields
from rest_framework import serializers
from misPerris.models import Mascota, Categoria

# definir una clase con la tabla a serializar y los
# campos
class MascotasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascota
        fields = ["nombre","edad","descripcion","imagen"]

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ["nombre","annos"]