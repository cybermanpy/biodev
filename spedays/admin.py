from django.contrib import admin
from .models import Speday
# Register your models here.

@admin.register(Speday)
class AdminSpeday(admin.ModelAdmin):
	list_display = ('id', 'userid', 'yuanying', 'startspecday', 'endspecday')
	list_filter = ('userid',)