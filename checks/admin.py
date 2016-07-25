from django.contrib import admin

from .models import Check
# Register your models here.

@admin.register(Check)
class AdminCheck(admin.ModelAdmin):
	list_display = ('id', 'userid', 'checktime', 'checktype',)
	list_filter = ('userid',)