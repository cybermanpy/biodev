from django.contrib import admin
from .models import Month

@admin.register(Month)
class AdminMonth(admin.ModelAdmin):
    list_display = ('id', 'number', 'denomination')