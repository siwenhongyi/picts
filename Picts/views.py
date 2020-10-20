import datetime

from django import forms
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import os
import random
import json

# my packagesnn


# Create your views here.
from App import settings
from Picts.models import Pict, Kind, User, TOPIC_CHOICES

path = '/Picts/static/background'


class LoginForm(forms.Form):
    user_id = forms.CharField(min_length=6,max_length=10,required=True,)
    nick_name = forms.CharField(required=True, error_messages={'required': '用户名不能为空'})
    password = forms.CharField(required=True,
                               min_length=6,
                               max_length=10,
                               error_messages={'required': '密码不能为空', 'min_length': '至少6位',
                                               'max_length': '至多10位'}
                               )
    city = forms.CharField(required=False, label='城市')
    sex = forms.CharField(required=False,label='性别')
    occupation =forms.CharField(required=False, label='职业')
    portrait =forms.URLField()






def init():
    f1 = os.listdir(os.getcwd() + path)
    kind_n = Kind.objects.all().count()
    kinds = Kind.objects.all()
    index = 1
    for i in f1:
        ran1 = random.randint(2, 3)
        model = Pict()
        model.pict_id = str(index)
        model.pic_url = os.path.join('background',i)
        kind_need = []
        model.save()
        while len(kind_need) != ran1:
            ran2 = random.randint(0, kind_n - 1)
            while kinds[ran2] in kind_need:
                ran2 = random.randint(0, kind_n - 1)
            model.kind.add(kinds[ran2])
            kind_need.append(kinds[ran2])
        index += 1
        model.save()


def index(request):
    # init()
    f = os.listdir(os.getcwd() + path)
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

def login(request):
    if request.POST:
        objPost = LoginForm(request.POST)
        ret = objPost.is_valid()
        if ret:
            print(objPost.clean())
        else:
            from django.forms.utils import ErrorDict
            print(type(objPost.errors),objPost.errors.as_json())
        return render(request, 'index.html', {'data': objPost})
    else:
        objGet = LoginForm()
        return render(request, 'login.html', {'data': objGet})

def register(request):
    if request.method == 'POST':
        pf = LoginForm(request.POST)
        if pf.is_valid():
            # 获取表单元素
            user_id = pf.cleaned_data['user_id']
            nick_name = pf.cleaned_data['nick_name']
            password = pf.cleaned_data['password']
            portrait = pf.cleaned_data['portrait']
            city = pf.cleaned_data['city']
            sex = pf.cleaned_data['sex']
            occupation = pf.cleaned_data['occupation']


            # 将表单写入数据库
            user = User()
            user.user_id = user_id
            user.nick_name = nick_name
            user.password = password
            user.portrait = portrait
            user.city = city
            user.sex = sex
            user.occupation = occupation

            user.save()
            # 返回注册成功页面
            return render(request,'index.html', {'portrait': portrait})
    else:
        pf = LoginForm()
    return render(request,'register.html', {'pf': pf})
def photo(request):
    search_photos = Pict()
    kind = Kind.objects.filter(kind_name=request.POST.get("information"))
    print(kind)
    search_photos = Pict.objects.filter(kind=kind[0])
    print(search_photos)
    return render(request,
                  'photo.html',
                  {
                      "photos": search_photos,
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
