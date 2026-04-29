from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import RecordLaptimeForm


class RecordLaptimeView(TemplateView):

    def __init__(self):
        self.params = {
            'title':'RecordLaptime',
            'message':'Your data:',
            'form': RecordLaptimeForm()
        }

    def get(self, request):
        return render(request, 'recordlaptime/index.html', self.params)
    
    def post(self, request):
        msg = 'あなたは、<br>' + request.POST['name'] + \
            ' (' + request.POST['age'] + \
            ') </b>さんです。<br>メールアドレスは<b>' + request.POST['mail'] + \
            '</b>ですね。'
        self.params['message'] = msg
        self.params['form'] = RecordLaptimeForm(request.POST)
        return render(request, 'recordlaptime/index.html', self.params)
