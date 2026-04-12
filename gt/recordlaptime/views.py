from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request, id, nickname):
    result = 'Your ID; ' + str(id) + ', name: "' \
        + nickname + '".'
    return HttpResponse(result)
