from django.shortcuts import redirect, render

from app.forms import EmployeeForm
from app.models import Employee

# Create your views here.

def index(request):
    employees = Employee.objects.all() 
    return render(request, 'index.html', {'employees': employees})

def destroy(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    
    return redirect('/')

def edit(request, id):  
    employee = Employee.objects.get(id=id)  
    return render(request,'edit.html', {'employee':employee})

def update(request, id):
    employee = Employee.objects.get(id=id)  
    
    form = EmployeeForm(request.POST, instance = employee)  
    
    if form.is_valid():  
        form.save()  
        return redirect("/") 
    
    return render(request, 'edit.html', {'employee': employee})


def addnew(request):
    form = EmployeeForm()
    
    if request.method == 'POST':
        form = EmployeeForm(request.POST)  
        
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/')  
            except:  
                pass
        
        return redirect('/')
    
    return render(request, 'addnew.html', {'form': form})