from django.shortcuts import render
from django.http import HttpResponse
from .forms import RecordLaptimeForm

# Create your views here.
def index(request):
    params = {
        'title':'recordlaptime/index',
        'message':'your data:',
        'form':RecordLaptimeForm()
    }
    if (request.method == 'POST'):
        params['message'] = '名前:' + request.POST['name'] + \
            '<br>メール:' + request.POST['mail'] +\
            '<br>年齢:' + request.POST['age']
        params['form'] = RecordLaptimeForm(request.POST)
    return render(request, 'recordlaptime/index.html', params)

def form(request):
    msg = request.POST['msg']
    params = {
        'title':'recordlaptime/form',
        'msg':'こんにちは、' + msg + 'さん。',
    }
    return render(request, 'recordlaptime/index.html',params)