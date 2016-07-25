# coding=utf-8

from django.http import HttpResponse
#from django.shortcuts import render
from django.template import loader
from .models import Userinfo
# Create your views here.


def viewChecks(request):
	title = 'Sistema de Marcación'
	users = Userinfo.objects.all()
	template = loader.get_template('view_checks.html')
	context = {
		'title': title,
		'users': users,
	}
	return HttpResponse(template.render(context, request))
