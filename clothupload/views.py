from django.shortcuts import render
from django.http import HttpResponse
from main.models import Cloth
def index(request):
    rent = Cloth.objects.filter(lenter = request.user) #Candidate의 area와 매개변수 area가 같은 객체만 불러오기
    context = {'rent' : rent}
    return render(request, 'clothupload/clothupload.html',context)