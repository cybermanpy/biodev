from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.formChecks, name='formChecks'),
    url(r'^list', views.viewAll, name='viewAll'),
    url(r'^calendar', views.calendario, name='calendario'),
    url(r'^json/(?P<ci>\w+)/$', views.ckeckJson, name='ckeckJson'),
]