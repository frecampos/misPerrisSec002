from django.conf.urls import url
from rest_framework import urlpatterns
from api import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^api/mascotas/$',views.MascotasViewSet.as_view()),
    url(r'^api/categorias/$',views.CategoriasViewSet.as_view()),
    url(r'^api/buscar_mascota/(?P<nombre>.+)/$',views.MascotaBuscarViewSet.as_view()),
]

urlpatterns=format_suffix_patterns(urlpatterns)