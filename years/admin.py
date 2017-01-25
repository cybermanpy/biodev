from django.contrib import admin
from .models import Year

@admin.register(Year)
class AdminYear(admin.ModelAdmin):
    list_display = ('id', 'description', )
