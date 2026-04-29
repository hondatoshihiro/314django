from django.shortcuts import render
from django.http import HttpResponse
from .models import Friend
from .forms import RecordLaptimeForm

def index(request):
    params = {
        'title':'RecordLaptime',
        'message': 'all friends.',
        'form': RecordLaptimeForm(),
        'data': [],
    }
    if (request.method == "POST"):
        num = request.POST['id']
        item = Friend.objects.get(id=num)
        params['data'] = [item]
        params['form'] = RecordLaptimeForm(request.POST)
    else:
        params['data'] = Friend.objects.all()
    return render(request, 'recordlaptime/index.html', params)
