from django.conf.urls import url
from .views_api import UsuarioSignUp, Address, VendedoresView


urlpatterns = [
   
    url(r'^signup/', UsuarioSignUp.as_view()),
    url(r'^address/', Address.as_view()),
    url(r'^vendedores/', VendedoresView.as_view())
]