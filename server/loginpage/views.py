# Create your views here.
# yourapp/views.py
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
#from .forms import LoginForm

def signup(request):
    return render(request, 'registration.html')
def login(request):
    return render(request, 'login.html')