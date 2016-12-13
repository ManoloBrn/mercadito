from django.conf.urls import url
from .views_api import UsuarioSignUp, Address


urlpatterns = [
   
    url(r'^signup/', UsuarioSignUp.as_view()),
    url(r'^address/', Address.as_view())
]