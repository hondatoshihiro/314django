from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    params = {
        'title':'recordlaptime/index',
        'msg':'お名前は？',
    }
    return render(request, 'recordlaptime/index.html', params)

def form(request):
    msg = request.POST['msg']
    params = {
        'title':'recordlaptime/form',
        'msg':'こんにちは、' + msg + 'さん。',
    }
    return render(request, 'recordlaptime/index.html',params)