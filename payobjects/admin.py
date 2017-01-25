from django.contrib import admin
from .models import PayObject, Earning

@admin.register(PayObject)
class AdminPayObject(admin.ModelAdmin):
    list_display = ('id', 'number', 'concept')

@admin.register(Earning)
class AdminEarning(admin.ModelAdmin):
    list_display = ('id', 'fkuserinfo', 'fkpayobject', 'amount', 'fkmonth', 'fkyear',)
    list_filter = ('fkuserinfo', 'fkpayobject', 'fkmonth', 'fkyear',)