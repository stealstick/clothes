from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from main.models import Cloth
def index(request):
    rent = Cloth.objects.filter(lenter = request.user) #Candidate의 area와 매개변수 area가 같은 객체만 불러오기
    context = {'rent' : rent}
    return render(request, 'clothupload/clothupload.html',context)

def upload(request):
    cloth_name = request.POST['cloth_name']
    size = request.POST['size']
    category = request.POST['category']
    bo_prize = request.POST['bo_prize']
    lent_prize = request.POST['lent_prize']
    cloth_img = request.FILES['cloth_img']
    cloth_intro= request.POST['cloth_intro']
    cloth_about = request.POST['cloth_about']
    clothupload =Cloth(cloth_name=cloth_name, size=size,category =category, bo_prize=bo_prize, lent_prize=lent_prize, cloth_img=cloth_img, cloth_intro=cloth_intro, cloth_about= cloth_about, owner = request.user )
    clothupload.save()
    return HttpResponseRedirect('/mypage')