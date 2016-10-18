from django.shortcuts import render
from django.http import HttpResponse
from .models import Account
import datetime

def index(request):
    return render(request, 'account/login.html')

def signup(request):
    return render(request, 'account/signup.html')