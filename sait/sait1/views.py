from django.shortcuts import render

# Create your views here.

def home_noAuth(request):
    return render(request, 'home_notAuth.html')

def home(request):
    return render(request, 'home.html')

def sales(request):
    return render(request, 'sales.html')

def katalogue(request):
    return render(request, 'katalogue.html')

def registration(request):
    return render(request, 'auth_/reg.html')

def login(request):
    return render(request, 'auth_/login.html')

def detal(request):
    return render(request, 'Detal_katalogue.html')