import datetime

from django.shortcuts import render
# my packages
from datetime import datetime
from django.http import HttpRequest


# Create your views here.
def index(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'Picts/index.html',
        {
            'title': 'Home',
            'year': datetime.now().year,
        }
    )
