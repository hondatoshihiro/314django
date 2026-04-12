from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    params = {
        'title':'recordlaptime/index',
        'msg':'これはサンプルで作ったページです。',
        'goto':'next',
    }
    return render(request, 'recordlaptime/index.html', params)

def next(request):
    params = {
        'title':'recordlaptime/next',
        'msg':'これはもう１つのサンプルページです。',
        'goto':'index',
    }
    return render(request, 'recordlaptime/index.html', params)
