from django.shortcuts import render
from django.http import HttpResponse
import datetime

def index(request):
    return render(request, 'account/login.html')

def signup(request):
    return render(request, 'account/signup.html')