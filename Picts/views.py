import datetime

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import os
import random
import json

# my packages


# Create your views here.
from App import settings
from Picts.models import Pict,Kind

path = '/Picts/static/background'


def index(request):
    # f1 = os.listdir(os.getcwd()+path)
    # kind_n =  Kind.objects.all().count()
    # kinds = Kind.objects.all()
    # index =1
    # for i in f1:
    #     ran1 = random.randint(2,3)
    #     model = Pict()
    #     model.pict_id = str(index)
    #     model.pic_url = i
    #     kind_need = []
    #     model.save()
    #     for k in range(ran1):
    #         ran2 = random.randint(0, kind_n-1)
    #         while kinds[ran2] in kind_need:
    #             ran2 = random.randint(0, kind_n-1)
    #         model.kind.add(kinds[ran2])
    #         kind_need.append(kinds[ran2])
    #     index+=1
    # return HttpResponse('图片上传成功')
    f = os.listdir(os.getcwd()+path)
    cnt = len(f)
    x = random.randint(0, cnt)
    name = 'LOL_122.jpg'
    for i in range(cnt):
        if i == x:
            name = f[i]
            break
    return render(
        request,
        "index.html",
        {
            'title': "Home",
            'background_img_name': json.dumps([name]),
        }
    )
def person(request):
    return render(
        request,
        "person.html",
    )
def user(request):
    return render(
        request,
        "user.html",
    )
def photo(request):
    search_photos = Pict()
    kind = Kind.objects.filter(kind_name = request.POST.get("information"))
    print(kind)
    search_photos = Pict.objects.filter(kind=kind)
    return render(request,'photo.html',
                  {
                      'photos':search_photos
                  }
    )
def up_img(request):
    pic = request.FILES.get('picture')
    model = Pict()
    model.pict_id = "66"
    model.pic_url = pic
    print(model.pic_url)
    model.save()
    return HttpResponse('图片上传成功')

