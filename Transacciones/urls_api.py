from django.conf.urls import url
from .views_api import BillData

urlpatterns = [
    url(r'^create/', BillData.as_view()),
]