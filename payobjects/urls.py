from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^dashboard/earning/list/$', views.EarningList, name='listEarning'),
]