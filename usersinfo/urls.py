from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^users/views/$', views.viewUser, name='viewUser'),
    url(r'^users/views/certificate/(?P<ficha>[0-9]+)/$', views.viewCertificate, name='viewCertificate'),
]