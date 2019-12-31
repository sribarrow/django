from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
     return HttpResponse("App Two!")

def help(request):
    # return HttpResponse("Hello World!")
    help_dict = {'help':"This is my help view"}
    return render(request, 'AppTwo/help.html', context=help_dict)
