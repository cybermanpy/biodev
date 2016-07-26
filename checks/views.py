# coding=utf-8

from django.http import HttpResponse
from django.template import loader
from .forms import FormSearchCheck
from .models import Check
from usersinfo.models import Userinfo
import datetime
from django.db.models import Q
# from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger

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
            list1 = { 'm': month, 'y': year }
            list_check = Check.objects.filter(userid__ssn=ci, checktime__month=month, checktime__year=year).order_by('-checktime')
            # list_check = Check.objects.filter(Q(userid=cedula) | Q(checktime__month=m)).order_by('-checktime')
            context1 = {
                'title': title,
                'list_check': list_check,
                'list1': list1,
            }
            return HttpResponse(template1.render(context1, request))
    else:
        form = FormSearchCheck()
    context = {
        'title': title,
        'form': form,
    }
    return HttpResponse(template.render(context, request))

# def formChecks(request):
#     title = 'Sistema de Marcación'
#     template1 = loader.get_template('list_checks.html')
#     if request.method=='POST':
#         form=FormSearchCheck(request.POST)
#         if form.is_valid():
#             cedula=request.POST['cedula']
#             list_check = Check.objects.filter(userid=cedula).order_by('-checktime')
#             paginator = Paginator(list_check,10)
#             try:
#                 page = int(request.GET.get('page','1'))
#             except ValueError:
#                 page = 1
#             try:
#                 listCheck = paginator.page(page)
#             except (EmptyPage, InvalidPage):
#                 listCheck = paginator.page(paginator.num_pages)
#             return HttpResponse(template1.render({'title': title, ' listCheck': listCheck}, request))
#         else:
#             list_check = Check.objects.all()
#             paginator = Paginator(list_check,10)
#             try:
#                 page = int(request.GET.get('page','1'))
#             except ValueError:
#                 page = 1
#             try:
#                 list_check = paginator.page(page)
#             except (EmptyPage, InvalidPage):
#                 list_check = paginator.page(paginator.num_pages)
#             return HttpResponse(template1.render({'title': title, ' listCheck': listCheck}, request))
#     else:
#         form = FormSearchCheck()
#         template = loader.get_template('form_check.html')
#         context = {
#             'title': title,
#             'form': form,
#         }
#     return HttpResponse(template.render(context, request))