from django.shortcuts import render
from django.http import HttpResponse
from .models import Friend

def index(request):
    data = Friend.objects.all().values_list('id','name','age')
    params = {
        'title':'RecordLaptime',
        'data': data,
    }
    return render(request, 'recordlaptime/index.html', params)
