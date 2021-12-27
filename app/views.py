from django.shortcuts import render
from django.shortcuts import render, redirect,HttpResponse
from django import forms
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib import messages

from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import *
from .forms import *

def landingpage(request):
    return render(request, "landingpage.html")
    
def homepage(request):
    if request.method == 'POST':
        form = EmailChangeform(request.POST, instance=request.user)
        if form.is_valid():
            form.save()

            messages.success(request, ('Your profile was successfully updated!'))
            
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        form  = EmailChangeform(
            initial={
            'email':request.user.email,
            
            }
        )
    return render(request, 'homepage.html', {'form': form})

def LoginUser(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect("homepage")
    if request.POST:
        form    = UserLoginForm(request.POST)
        email   = request.POST.get('email')
        password = request.POST.get('password')
        user =  authenticate(email=email, password=password)
        if user:
            auth_login(request, user)
            messages.success(request, "Logged In")
            return redirect("homepage")
        else:
            messages.info(request, 'Username OR password is incorrect')
    else:
        form = UserLoginForm()
    context['login_form'] = form
    return render(request, "login.html", context)

def register(request):
    
    if request.method == 'POST':

        form = registerForm(request.POST)
       

        if form.is_valid():
            form.save()
            
            
            messages.success(request,('Your User was successfully Created!'))
            
        else:
            messages.error(request,('Please correct the error below.'))
    else:
        form = registerForm()
        
    return render(request, 'register.html', {'register_form': form})


def logoutUser(request):
    logout(request)
    return redirect('login')

#update all user info
def user_profile(request):
    if request.method == 'POST':
        form = ProfileUpdateform(request.POST, instance=request.user)
        if form.is_valid():
            form.save()

            messages.success(request, ('Your profile was successfully updated!'))
            
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        form  = ProfileUpdateform(
            initial={
            'last_name':request.user.last_name,
            'first_name':request.user.first_name,
            'email':request.user.email,
            
            }
        )
    return render(request, 'homepage.html', {'form': form})
