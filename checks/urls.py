from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.formChecks, name='formChecks'),
    url(r'^list', views.viewAll, name='viewAll'),
    url(r'^calendar', views.calendario, name='calendario'),
    url(r'^form/$', views.getForm, name='getForm'),
    url(r'^form/ajax/$', views.formParam, name='formParam'),
    url(r'^json/(?P<ci>\w+)/(?P<month>[0-9]+)/(?P<year>[0-9]+)/$', views.ckeckJson, name='ckeckJson'),
]