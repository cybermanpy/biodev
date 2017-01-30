from django.contrib import admin
from .models import Line

@admin.register(Line)
class AdminLine(admin.ModelAdmin):
    list_display = ('id', 'number', )