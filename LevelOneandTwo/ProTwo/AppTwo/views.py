from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User
# Create your views here.

def index(request):
     return HttpResponse("App Two!")

def help(request):
    # return HttpResponse("Hello World!")
    help_dict = {'help':"This is my help view"}
    return render(request, 'AppTwo/help.html', context=help_dict)

def users(request):
    users_list = User.objects.order_by('first_name')
    user_dict = {'users': users_list}
    # return HttpResponse("Hello World!")
    # my_dict = {'insert_me':"Updated from firstapp/index.html"}
    return render(request, 'AppTwo/users.html', context=user_dict)
