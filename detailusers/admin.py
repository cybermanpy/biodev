from django.contrib import admin
from .models import Detailuser

@admin.register(Detailuser)
class AdminDetailuser(admin.ModelAdmin):
    list_display = ('id', 'line', 'email', 'fkuserinfo' )