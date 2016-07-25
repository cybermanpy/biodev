from django.contrib import admin
from .models import Userinfo #, Checks
# Register your models here.

@admin.register(Userinfo)
class AdminUserInfo(admin.ModelAdmin):
	list_display = ('userid', 'badgenumber', 'name', 'ssn', )
	list_filter = ('defaultdeptid',)

# @admin.register(Checks)
# class AdminChecks(admin.ModelAdmin):
# 	list_display = ('userid', 'checktime', 'checktype',)
# 	list_filter = ('userid',)