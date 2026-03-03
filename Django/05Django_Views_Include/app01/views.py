from django.shortcuts import render

# Create your views here.

def app01_index(request):
    userData = {
        'name': 'John Doe',
        'age': 30,
        'email': 'john.doe@example.com'
    }
    
    return render(request, 'app01_Templates/index.html', {'user': userData})