# coding=utf-8

from django.http import HttpResponse
#from django.shortcuts import render
from django.template import loader
from .models import Userinfo
# Create your views here.


def viewUser(request):
	title = 'Sistema de Marcación'
	users = Userinfo.objects.all().order_by('badgenumber')
	template = loader.get_template('view_user.html')
	context = {
		'title': title,
		'users': users,
	}
	return HttpResponse(template.render(context, request))

def viewCertificate(request, ficha):
    title = 'constancia de ingresos'
    user = Userinfo.objects.filter(badgenumber=ficha)
    template = loader.get_template('view_certificate.html')
    context = {
        'title': title,
        'user': user,
    }
    return HttpResponse(template.render(context, request))
