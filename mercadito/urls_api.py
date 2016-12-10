from django.conf.urls import url, include

urlpatterns = [
    url(r'^productos/', include("Inventarios.urls_api"))
]