from django.contrib import admin
from .models import PayObject, Earning
from actions import export_xls, export_csv, export_xlsx

@admin.register(PayObject)
class AdminPayObject(admin.ModelAdmin):
    list_display = ('id', 'number', 'concept')

@admin.register(Earning)
class AdminEarning(admin.ModelAdmin):
    list_display = ('id', 'fkuserinfo', 'fkpayobject', 'amount', 'fkmonth', 'fkyear', 'date')
    list_filter = ('fkuserinfo', 'fkpayobject', 'fkmonth', 'fkyear')
    search_fields = ('fkuserinfo__name',)
    actions = [export_xls, export_csv, export_xlsx]