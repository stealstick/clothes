from django.shortcuts import render
from django.http import HttpResponse
from .models import Account
import datetime

def index(request):
    return render(request, 'account/login.html')

def signup(request):
    return render(request, 'account/signup.html')

# index 함수 유지

def login(request):
    userid = request.POST['userid']
    userpw = request.POST['userpw']
    user = Account.objects.get(userid = userid, userpw = userpw)
    context = { 'user': user }
    return render(request, 'main/index.html', context)