import datetime

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import os
import random
import json

# my packages


# Create your views here.
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


def user(request):
    return render(
        request,
        "user.html",
    )
