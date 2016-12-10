from django.conf.urls import url
from .views_api import ProductosList,ProductosCreate


urlpatterns = [
    url(r'^list/', ProductosList.as_view({'get':'list'})),
    url(r'^create/', ProductosCreate.as_view()),
    
]