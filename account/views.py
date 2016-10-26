from django.shortcuts import render
from django.http import HttpResponse
from .models import User
import datetime

def index(request):
    return render(request, 'account/login.html')

def signup(request):
    return render(request, 'account/signup.html')

def useradd(request):
    username = request.POST['username']
    password = request.POST['password']
    name = request.POST['name']
    email = request.POST['email']
    phone_number = request.POST['phone_number']
    area = request.POST['email']
    useradd = User(username=username, password=password,name=name, email=email, phone_number=phone_number)
    useradd.set_password(password)
    useradd.save()
    return render(request, 'account/login.html')