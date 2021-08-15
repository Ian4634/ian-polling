from django.shortcuts import render,redirect
from django.contrib.auth.models import User 
from django.contrib import auth
from django.contrib import messages
# Create your views here.
def register(request):
    return render(request,'register.html')

def verify(request):
    username = request.POST['username']
    password = request.POST['password']
    comfirm_password = request.POST['comfirm_password']
    if password == comfirm_password:
        if User.objects.filter(username=username).exists():
            messages.info(request, 'username used')
            return redirect('/')
        else:
            create_user = User.objects.create_user(username=username,password=password)
            create_user.save()
            return redirect('/login/')
    else:
        return redirect('/')

def login(request):
    return render(request,'login.html',)

def inspect_login(request):
    username = request.POST['user']
    password = request.POST['password']

    user = auth.authenticate(request,username=username,password=password)
    if user is not None:
        auth.login(request,user)
        return redirect('/home/'+username+'/')
    else:
        messages.info(request,'invalid credentials')
        return redirect('/login/')
def home(request,username):
    #returns True or False
    is_authenticated = request.user.is_authenticated 
    user = request.user.username
    if is_authenticated:
        return render(request,'home.html',{"t":is_authenticated,'user':user})
    else:
        return redirect('/')
def logout(request):
    username = request.POST['username']
    auth.logout(request)
    return redirect('/')

def polling(request,username):
    return redirect('/polling/'+username+'/')