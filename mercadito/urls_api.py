from django.conf.urls import url, include

urlpatterns = [
    url(r'^productos/', include("Inventarios.urls_api")),
    url(r'^usuarios/', include("Usuarios.urls_api"))
]