from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django import forms
from django.contrib.auth.models import User
from .models import Record
# Create your views here.
def home(request):
    records = Record.objects.all()
    #check to see if the user login in 
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"You Have Been Logged In Successfully")
            return redirect('home')
        else:
            messages.success(request,"There Was an error Logged In Please Try Again... ")
            return redirect('home')
    else:
        return render(request,'home.html',{'records':records})

# def login_user(request):
#     pass

def logout_user(request):
    logout(request)
    messages.success(request,"You Have Been Logged out....")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 == password2:
            if User.objects.filter(username=username).exists():
               messages.info(request,'username taken already')
               return redirect('register') 
            
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('register')   
            else:
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                messages.info(request,'user created') 
                return redirect('home')
        else:
            messages.info(request,'password not matching')
            return redirect('register')
    else:
        return render(request,'register.html')