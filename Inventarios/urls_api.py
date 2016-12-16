from django.conf.urls import url
from .views_api import ProductosList,ProductosCreate,ProductoUsuario


urlpatterns = [
    url(r'^list/', ProductosList.as_view({'get':'list'})),
    url(r'^create/', ProductosCreate.as_view()),
    url(r'^vendedor/(?P<pk>[0-9]+)/', ProductoUsuario.as_view())
    
]