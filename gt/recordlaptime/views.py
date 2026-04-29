from django.shortcuts import render
from django.http import HttpResponse
from .models import Friend

def index(request):
    data = Friend.objects.all()
    params = {
        'title':'RecordLaptime',
        'message': 'all friends.',
        'data': data,
    }
    return render(request, 'recordlaptime/index.html', params)
