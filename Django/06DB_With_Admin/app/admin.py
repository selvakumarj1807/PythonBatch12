from django.contrib import admin

from app.models import Departments, Employee

# Register your models here.

admin.site.register(Employee)
admin.site.register(Departments)