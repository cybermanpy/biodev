# coding=utf-8

from django.http import HttpResponse #, Http404
from django.template import loader
from .forms import FormSearchCheck
from .models import Check
from usersinfo.models import Userinfo
from django.core.exceptions import ObjectDoesNotExist
# from django.db.models import Q
# from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger

from datetime import datetime
import calendar
from django.shortcuts import get_object_or_404
# import json
from django.core import serializers
# Create your views here.

def formChecks(request):
    title = 'Sistema de Marcación'
    template = loader.get_template('form_check.html')
    template1 = loader.get_template('list_checks.html')
    if request.method == 'POST':
        form = FormSearchCheck(request.POST)
        if form.is_valid():
            ci = request.POST['ci']
            month = request.POST['month']
            year = request.POST['year']
            option = request.POST['options']
            list1 = { 'm': month, 'y': year }
            try:
                # list_check = Check.objects.filter(userid__ssn=ci, checktime__month=month, checktime__year=year).order_by('-checktime')
                if option == '1':
                    getuser = Userinfo.objects.get(ssn=ci)
                elif option == '2':
                    getuser = Userinfo.objects.get(badgenumber=ci)
                # getuser = Userinfo.objects.get(ssn=ci)
                name = getuser.name
                pkuser = getuser.userid
                list_check = Userinfo.objects.filter(userid=pkuser, check__userid=pkuser, check__checktime__month=month, check__checktime__year=year).values('check__checktime').order_by('check__checktime')
                list_speday = Userinfo.objects.filter(userid=pkuser, speday__userid=pkuser, speday__startspecday__month=month, speday__startspecday__year=year).values('speday__startspecday', 'speday__yuanying', 'speday__endspecday').order_by('speday__startspecday')
            except ObjectDoesNotExist:
                error = "El numero de cedula o la ficha es incorrecto"
                templateError = loader.get_template('error.html')
                contextError = {
                    'title': title,
                    'error': error,
                }
                return HttpResponse(templateError.render(contextError, request))
            # for li in list_check:
            #     name = li.userid.name
            # list_check = Check.objects.filter(Q(userid=cedula) | Q(checktime__month=m)).order_by('-checktime')
            context1 = {
                'title': title,
                'list_check': list_check,
                'list_speday': list_speday,
                'list1': list1,
                'name': name,
            }
            return HttpResponse(template1.render(context1, request))
    else:
        form = FormSearchCheck()
    context = {
        'title': title,
        'form': form,
    }
    return HttpResponse(template.render(context, request))

def viewAll(request):
    title = 'Sistema de Marcación'
    # list_user = Userinfo.objects.filter(check__userid=94, check__checktime__month=8).values('name', 'ssn', 'check__checktime').order_by('-check__checktime')
    list_user = Userinfo.objects.filter(speday__userid=94, speday__startspecday__month=8).values('speday__startspecday', 'speday__yuanying', 'speday__endspecday').order_by('-speday__startspecday')
    # template = loader.get_template('list_user.html')
    template = loader.get_template('list_speday.html')
    context = {
        'title': title,
        'list_user': list_user,
    }
    return HttpResponse(template.render(context, request))



def calendario(request):
    title = 'Calendario'
    template = loader.get_template('calendar.html')
    checkList = Check.objects.filter(userid=86, checktime__month=12, checktime__year=2016)
    # years = date.today().year
    # months = date.today().month
    # calendario = calendar.month(years, months)
    marcacion = {}

    a = iter(list(checkList))
    for i in a:
        marcacion[i.checktime.day] = [i.checktime.hour, next(a)]
    
    # for item in checkList:
    #     marcacion['lunes'] = [item.checktime.hour]
       
    # matriz = []
    # for item in checkList:
    #     matriz.append(item.checktime.hour)

    # context = {
    #     'title': title,
    #     'calendario': calendario,
    # }
    context = {
        'title': title,
        'checkList': checkList,
        'marcacion': marcacion,

    }
    return HttpResponse(template.render(context, request))

def ckeckJson(request, ci):
    user = get_object_or_404(Userinfo, ssn=ci)
    pkuser = user.userid
    # checkList = get_object_or_404(Check, userid=ci, checktime__day=12, checktime__month=12, checktime__year=2016)
    # pkuser = user.userid
    checkList = Check.objects.filter(userid=pkuser, checktime__month=12, checktime__year=2016)
    # checkList = Userinfo.objects.filter(userid=pkuser, check__userid=pkuser, check__checktime__year=2016, check__checktime__month=12, check__checktime__day=12)
    # checkList = Userinfo.objects.filter(userid=pkuser, check__userid=pkuser, check__checktime__month=12, check__checktime__year=2016).values('check__checktime').order_by('check__checktime')
    jsonData = serializers.serialize('json', checkList)
    # data = {
    #    'id': check.userid,
    #    'checktime': check.checktime,
    # }
    # jsonData = json.dumps(data)
    # json.loads(string_json) para convertir json a un diccionario de python
    return HttpResponse(jsonData, content_type="application/json")

# def formChecks(request):
#     title = 'Sistema de Marcación'
#     template = loader.get_template('form_check.html')
#     template1 = loader.get_template('list_checks.html')
#     if request.method=='POST':
#         form=FormSearchCheck(request.POST)
#         if form.is_valid():
#             ci=request.POST['ci']
#             month = request.POST['month']
#             year = request.POST['year']
#             list1 = { 'm': month, 'y': year }
#             list_check = Check.objects.filter(userid__ssn=ci, checktime__month=month, checktime__year=year).order_by('-checktime')
#             paginator = Paginator(list_check,10)
#             try:
#                 page = int(request.GET.get('page','1'))
#             except ValueError:
#                 page = 1
#             try:
#                 listCheck = paginator.page(page)
#             except (EmptyPage, InvalidPage):
#                 listCheck = paginator.page(paginator.num_pages)

#             for li in list_check:
#                 name = li.userid.name

#             context1 = {
#                 'title': title,
#                 'listCheck': listCheck,
#                 'name': name,
#                 'list1': list1,
#             }
#             return HttpResponse(template1.render(context1, request))
#         # else:
#         #     list_check = Check.objects.all()
#         #     paginator = Paginator(list_check,10)
#         #     try:
#         #         page = int(request.GET.get('page','1'))
#         #     except ValueError:
#         #         page = 1
#         #     try:
#         #         list_check = paginator.page(page)
#         #     except (EmptyPage, InvalidPage):
#         #         list_check = paginator.page(paginator.num_pages)
#         #     context1 = {
#         #         'title': title,
#         #         'listCheck': listCheck
#         #     }
#         #     return HttpResponse(template1.render(context1, request))
#     else:
#         form = FormSearchCheck()
#     context = {
#         'title': title,
#         'form': form,
#     }
#     return HttpResponse(template.render(context, request))