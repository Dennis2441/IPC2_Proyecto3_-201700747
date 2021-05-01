from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def Principal(request):
    return render(request, 'Principal.html')