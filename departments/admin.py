from django.contrib import admin
from .models import Department
# Register your models here.

@admin.register(Department)
class AdminDeparment(admin.ModelAdmin):
	list_display = ('deptid', 'deptname',)
	list_filter = ('deptname',)