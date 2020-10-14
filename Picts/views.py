import datetime

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import os
import random
import json

# my packages


# Create your views here.
from Picts.models import Pict,Kind

path = '/Picts/static/background'


def index(request):
    assert (request, HttpRequest)
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