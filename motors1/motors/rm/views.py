from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'home.html')
def signup(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        if not User.objects.filter(username=username):
            User.objects.create_user(username=username,email=email,password=password)
            return redirect('/login')
        else:
            messages.error(request,'user already exists')
    return render(request,'signup.html')
def signin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('view')
        else:
            messages.error(request,"Invalid login credentials")
    return render(request,'login.html')
@login_required()
def view(request):
    cust=Motors.objects.all()
    return render(request,'view.html',{'cu':cust})
def signout(request):
    logout(request)
    return redirect('home')
