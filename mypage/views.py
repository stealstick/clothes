from django.shortcuts import render
from django.http import HttpResponse
from main.models import Cloth
import datetime

def index(request):
    my_cloth= Cloth.objects.filter(owner=request.user)
    rent = Cloth.objects.filter(lenter = request.user)
    context = {'my_cloth': my_cloth,
    'rent' : rent}
    return render(request, 'mypage/mypage.html', context)