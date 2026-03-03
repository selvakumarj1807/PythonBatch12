from django.shortcuts import render

# Create your views here. 

def app02_index(request):
    return render(request, 'app02_templates/index.html')