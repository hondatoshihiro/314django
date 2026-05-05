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
    if request.method == 'POST':
        obj = Friend()
        recordlaptime = RecordLaptimeForm(request.POST, instance=obj)
        recordlaptime.save()
        return redirect(to='/recordlaptime')
    params = {
        'title': 'RecordLaptime',
        'form': RecordLaptimeForm(),
    }
    return render(request, 'recordlaptime/create.html', params)

def edit(request, num):
    obj = Friend.objects.get(id=num)
    if request.method == "POST":
        recordlaptime = RecordLaptimeForm(request.POST, instance=obj)
        recordlaptime.save()
        return redirect(to='/recordlaptime')
    params = {
        'title': 'RecordLaptime',
        'id': num,
        'form': RecordLaptimeForm(instance=obj),
    }
    return render(request, 'recordlaptime/edit.html', params)

def delete(request, num):
    friend = Friend.objects.get(id=num)
    if request.method == "POST":
        friend.delete()
        return redirect(to='/recordlaptime')
    params = {
        'title': 'RecordLaptime',
        'id': num,
        'obj': friend,
    }
    return render(request, 'recordlaptime/delete.html', params)
    