from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    params = {
        'title':'recordlaptime/index.html',
        'msg':'これはサンプルで作ったページです。',
    }
    return render(request, 'recordlaptime/index.html', params)