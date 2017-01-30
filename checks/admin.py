from django.contrib import admin

from .models import Check
from actions import export_xls, export_csv, export_xlsx


@admin.register(Check)
class AdminCheck(admin.ModelAdmin):
    list_display = ('id', 'userid', 'checktime', 'checktype',)
    list_filter = ('userid',)
    actions = [export_xls, export_csv, export_xlsx]