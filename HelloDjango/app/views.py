from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def index(request):
    return render(request , 'Base.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'regiseter.html')

def profile(request):
    return render(request,'profile.html')