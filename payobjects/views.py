from django.http import HttpResponse
from django.template import loader
from .models import Earning

def EarningList(request):
    title = 'Informe de Pagos'
    template = loader.get_template('earning_list.html')
    object_list = Earning.objects.all().order_by('fkuserinfo__name', 'fkmonth__number', 'fkpayobject__number')
    context = {
        'title': title,
        'object_list': object_list,
    }
    return HttpResponse(template.render(context, request))