from django.shortcuts import render
from django.http import HttpResponse
from .models import Cloth
def index(request):
    try :
        rent = Cloth.objects.filter(lenter = request.user)        
    except:
        rent = None;
    clothes = Cloth.objects.all()

    context = {'clothes': clothes,
    'rent' : rent}
    return render(request, 'main/main.html', context)

def category(request, category):
    category_item= Cloth.objects.filter(category=category)

    try :
        rent = Cloth.objects.filter(lenter = request.user)        
    except:
        rent = None;
    context = {'category_item': category_item,
    'rent' : rent,
    'category' : category}

    return render(request, 'main/category.html', context)

def send(request, username):
    context = {'username' : username}
    return render(request, 'main/send.html', context)