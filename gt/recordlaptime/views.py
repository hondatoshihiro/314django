from django.shortcuts import render
from django.http import HttpResponse
from .models import Friend

def index(request):
    num = Friend.objects.all().count()
    first = Friend.objects.all().first()
    second = Friend.objects.all().last()
    data = [num, first, second]
    params = {
        'title':'RecordLaptime',
        'data': data,
    }
    return render(request, 'recordlaptime/index.html', params)
