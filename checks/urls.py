from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.formChecks, name='formChecks'),
    url(r'^list', views.viewAll, name='viewAll'),
]