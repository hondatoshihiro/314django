from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Friend
from .forms import RecordLaptimeForm

def index(request):
    data = Friend.objects.all()
    params = {
        'title':'RecordLaptime',
        'data': data,
    }
    return render(request, 'recordlaptime/index.html', params)

def create(request):
    params = {
        'title': 'RecordLaptime',
        'form': RecordLaptimeForm(),
    }
    if request.method == 'POST':
        name = request.POST['name']
        mail = request.POST['mail']
        gender = 'gender' in request.POST
        age = int(request.POST['age'])
        birth = request.POST['birthday']
        friend = Friend(name = name, mail = mail, gender = gender, age = age, birthday = birth)
        friend.save()
        return redirect(to='/recordlaptime')
    return render(request, 'recordlaptime/create.html', params)
