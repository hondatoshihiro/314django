from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import RecordLaptimeForm


class HelloView(TemplateView):

    def __init__(self):
        self.params = {
            'title':'RecordLaptime',
            'message':'Your data:',
            'form': RecordLaptimeForm()
        }

    def get(self, request):
        return render(request, 'recordlaptitme/index.html', self.params)
    
    def post(self, request):
        msg = 'あなたは、<br>' + request.POST['name'] + \
            ' (' + request.POST['age'] + \
            ') </b>さんです。<br>メールアドレスは<b>' + request.POST['mail'] + \
            '</b>ですね。'
        self.params['message'] = msg
        self.params['form'] = RecordLaptimeForm(request.POST)
        return render(request, 'recordlaptime/index.html', self.params)

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