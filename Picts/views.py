import datetime

from django.shortcuts import render
from django.http import  HttpResponse
# my packages


# Create your views here.
def index(request ):
    return render(
        request,
        "index.html"
    )


def user(request):
    return render(
        request,
        "user.html"
    )