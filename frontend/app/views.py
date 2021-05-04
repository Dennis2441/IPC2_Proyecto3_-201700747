from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def Principal(request):
    return render(request, 'Principal.html')
def fecha(request):

    return render(request, 'fecha.html')
    
def codigo(request):
    return render(request, 'codigo.html')