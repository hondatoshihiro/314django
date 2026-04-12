from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    apName = 'On RecordLapTime AP '
    if 'msg' in request.GET:
        msg = request.GET['msg']
        result = apName + 'You typed: "' + msg + '".'
    else:
        result = apName + 'Please send msg parameter!'
    return HttpResponse(result)
