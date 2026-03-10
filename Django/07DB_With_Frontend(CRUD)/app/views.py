from django.shortcuts import render

from app.models import Employee

# Create your views here.

def index(request):
    employees = Employee.objects.all() 
    return render(request, 'index.html', {'employees': employees})