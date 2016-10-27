from django.shortcuts import render
from django.http import HttpResponse
from .models import Cloth
def index(request):
    clothes = Cloth.objects.all()
    rent = Cloth.objects.filter(lenter = request.user) #Candidate의 area와 매개변수 area가 같은 객체만 불러오기
    context = {'clothes': clothes,
    'rent' : rent}
    return render(request, 'main/main.html', context)

def category(request, category):
    category_item= Cloth.objects.filter(category=category)
    rent = Cloth.objects.filter(lenter = request.user)
    context = {'category_item': category_item,
    'rent' : rent,
    'category' : category}
    return render(request, 'main/category.html', context)