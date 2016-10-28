from django.shortcuts import render
from django.http import HttpResponse
from main.models import Cloth

def index(request, cloth_name):
    cloth= Cloth.objects.get(cloth_name=cloth_name)
    rent = Cloth.objects.filter(lenter = request.user) #Candidate의 area와 매개변수 area가 같은 객체만 불러오기
    context = {'cloth':cloth,
    'rent' : rent}
    return render(request, 'clothdetail/clothdetail.html', context)
# Create your views here.
