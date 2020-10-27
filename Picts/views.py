import datetime

from django import forms
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, JsonResponse
from django.forms.boundfield import BoundField
import os
import random
import json

# my packagesnn


# Create your views here.
from django.urls import reverse
from django.views.generic.base import View

from App import settings
from Picts.models import *

path = '/Picts/static/background'


class login(View):
    def get(self, request, *args, **kwargs):
        return render(request, ' login.html', locals())

    def post(self, request, *args, **kwargs):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username ']
            password = login_form.cleaned_data[' password']
            user = authenticate(username=username, pasSword=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('index'))
            else:
                return render(request, 'login.html', {'msg': '用户 名或密码错误', 'login form': login_form})
        else:
            return render(request, 'login.html', {'login_ form': login_form})


class LoginForm(forms.Form):
    user_id = forms.CharField(min_length=6, max_length=10, required=True)
    nick_name = forms.CharField(required=False, error_messages={'required': 'user_id not null'})
    password = forms.CharField(required=True,
                               min_length=6,
                               max_length=10,
                               error_messages={'required': 'password not null', 'min_length': 'min_length = 6',
                                               'max_length': 'max_length = 10'}
                               )
    city = forms.CharField(required=False, label='城市')
    sex = forms.CharField(required=False, label='性别')
    occupation = forms.CharField(required=False, label='职业')
    portrait = forms.URLField(required=False)


def init():
    f1 = os.listdir(os.getcwd() + path)
    kind_n = Kind.objects.all().count()
    kinds = Kind.objects.all()
    index = 1
    for i in f1:
        ran1 = random.randint(2, 3)
        model = Pict()
        model.pict_id = str(index)
        model.pic_url = os.path.join('background', i)
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


def HttpCookie(param):
    pass


def login(request):
    if request.method == "POST":
        objPost = LoginForm(request.POST)
        ret = objPost.is_valid()
        if not ret:
            print(type(objPost.errors), objPost.errors.as_json())
            return render(request, 'index.html', {'data': objPost})
        else:
            data = objPost.cleaned_data
            user = User.objects.filter(user_id=data["user_id"])
            if len(user) == 1 and user[0].password == data["password"]:
                secure = random.randint(0, 100000)
                response = HttpResponseRedirect('/index/')
                response.set_cookie('user_id', user[0].user_id, 3600)
                print(user[0].user_id)
                response.set_cookie('portrait', user[0].portrait, 3600)
                response.set_cookie('IS_LOGIN', True, 3600)
                response.set_cookie('token', secure, 3600)
                request.session['token'] = secure
                return response
            else:
                return render(request, 'login.html', {'data': LoginForm()})
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
            return render(request, 'index.html', {'portrait': portrait})
    else:
        pf = LoginForm()
    return render(request, 'register.html', {'pf': pf})


def photo(request):
    search_photos = Pict()
    kind = Kind.objects.filter(kind_name=request.POST.get("information"))
    search_photos = Pict.objects.filter(kind=kind[0])
    user_id = request.COOKIES.get('user_id', "")
    return render(request,
                  'photo.html',
                  {
                      "photos": search_photos,
                      "user_id": user_id,
                  }
                  )


def change_like(request):
    user_id = request.POST.get('user', "")
    pict_id = request.POST.get('pict_id')
    picts = Pict.objects.filter(pict_id=pict_id)
    user = User.objects.filter(user_id=user_id)
    data = dict()
    need = True
    if len(picts) != 1:
        data['pict_lens'] = len(picts)
        need = need and False
    if len(user) != 1:
        data['user_id'] = len(user)
        need = need and False
    if need:
        pict = picts.first()
        user = user.first()
        data['status'] = 'OK'
        if request.POST.get("status","") == 'add':
            pict.love_num += 1
            new_like = Collection()
            new_like.user_id = user
            new_like.pict_id = pict
            new_like.save()
            pict.save()
        else:
            for i in Collection.objects.filter(user_id=user.user_id, pict_id=pict.pict_id):
                i.pict_id.love_num -= 1
                i.pict_id.save()
                i.delete()
    return JsonResponse(data)


def up_img(request):
    pic = request.FILES.get('picture')
    model = Pict()
    model.pict_id = "66"
    model.pic_url = pic
    print(model.pic_url)
    model.save()
    return HttpResponse('图片上传成功')
