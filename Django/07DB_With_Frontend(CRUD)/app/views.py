from django.shortcuts import redirect, render

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
    
    if request.method == "POST":
        employee.name = request.POST.get('name')
        employee.email = request.POST.get('email')
        employee.contact = request.POST.get('contact')
        employee.save()
        
        return redirect('/')
    
    return render(request, 'edit.html', {'employee': employee})


def addnew(request):
    
    if request.method == "POST":
        employee = Employee()
        
        employee.name = request.POST.get('name')
        employee.email = request.POST.get('email')
        employee.contact = request.POST.get('contact')
        employee.save()
        
        return redirect('/')
        
    return render(request, 'addnew.html')