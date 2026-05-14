from django.shortcuts import render
# Create your views here.


def home(request):
    return render(request, 'home.html')

def notFound(request):
    return render(request, '404.html')
