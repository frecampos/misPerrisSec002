from django.shortcuts import render
    # dispone de paginas pre-diseñadas para presentar datos
from rest_framework import generics
    # indica el model y campos a serializar
from .serializers import CategoriaSerializer, MascotasSerializer
    # cuales seran los datos disponibles en la pagina
from misPerris.models import Mascota, Categoria


# Create your views here.

class MascotasViewSet(generics.ListAPIView):
    # cuales son los datos a mostrar
    queryset = Mascota.objects.all()
    # como seran serializados
    serializer_class = MascotasSerializer

class CategoriasViewSet(generics.ListAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class MascotaBuscarViewSet(generics.ListAPIView):
    serializer_class = MascotasSerializer
    def get_queryset(self):
        nombre_mascota = self.kwargs['nombre']
        return Mascota.objects.filter(nombre=nombre_mascota)