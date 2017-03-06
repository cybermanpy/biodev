from django.contrib import admin
from .models import Userinfo #, Checks
from actions import export_xls, export_csv, export_xlsx

@admin.register(Userinfo)
class AdminUserInfo(admin.ModelAdmin):
    list_display = ('userid', 'badgenumber', 'name', 'ssn', 'full_name')
    list_filter = ('defaultdeptid',)
    search_fields = ('name', )
    actions = [export_xls, export_csv, export_xlsx]


# @admin.register(Checks)
# class AdminChecks(admin.ModelAdmin):
#   list_display = ('userid', 'checktime', 'checktype',)
#   list_filter = ('userid',)