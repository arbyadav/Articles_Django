#1
from django.shortcuts import render, render_to_response
#2
from django.http import HttpResponseRedirect
#3.
from django.contrib import auth
#4.
from django.template.context_processors import csrf
#5.
from django.contrib.auth.forms import UserCreationForm

from .forms import MyRegistrationForm

def home(request):
    return render(request,"home.html")

def login(request):
    c={}
    c.update(csrf(request))
    return render_to_response('login.html',c)

def auth_view(request):
    username= request.POST.get('username','')
    password= request.POST.get('password','')
    user=auth.authenticate(username=username,password=password)
    
    if user is not None:
        auth.login(request,user)
        return HttpResponseRedirect('/accounts/loggedin')      
    else:
        return HttpResponseRedirect("/accounts/invalidlogin")
        
def loggedin(request):
    return render_to_response('loggedin.html',{'full_name':request.user.username})
      
def invalidlogin(request):
    return render_to_response('invalidlogin.html')

def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')

def register_user(request):
    if request.method=='POST':
        form=MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/accounts/register_success/")
    args={}
    args.update(csrf(request))
    
    args['form']=MyRegistrationForm()
    print(args)
    return render_to_response('register.html',args)

def register_success(request):
    return render_to_response('register_success.html')

