from django.conf.urls import url
from .views_api import BillData, BillList, BillIdList

urlpatterns = [
    url(r'^create/', BillData.as_view()),
    url(r'^list/', BillList.as_view()),
     url(r'^bill/(?P<pk>[0-9]+)/', BillIdList.as_view())
]