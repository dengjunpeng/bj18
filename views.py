from django.http import HttpResponse
from django.shortcut import redirect

def index(request):
    return HttpResponse('index')

def login(request):
    return redirect('/index')

