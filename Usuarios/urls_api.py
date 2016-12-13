from django.conf.urls import url
from .views_api import UsuariosCreate, Address


urlpatterns = [
   
    url(r'^create/', UsuariosCreate.as_view()),
    url(r'^address/', Address.as_view())
]