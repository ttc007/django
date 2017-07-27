# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib import auth
from django.contrib.auth.models import User
from character.models import Character
from login.forms import *
from pprint import pprint

def login_view(request):
    return render(request, 'login/login.html')
def login(request):
    # if request.user.is_authenticated():
    #     return HttpResponseRedirect("/")
    # else:
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        # print_r(user)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return redirect('/')
    error = "Wrong username or password"
    return render(request, 'login/login.html',{'error':error})
def logout(request):
    auth.logout(request)
    return redirect('/')
def register_view(request):
    registerForm = RegisterForm() 
    return render(request, 'login/register.html',{'form':registerForm})
def register(request):
    print("get")
    username = request.POST['username']
    password = request.POST['password']
    password_again=request.POST['password_again']
    email=request.POST['email']
    # pprint(request)
    print(username,password,email)
    if password==password_again:
        user = User.objects.create_user(username, email, password)
        return redirect("/")
    error="Password Again not match"
    return render(request, 'login/register.html',{'error':error})
def createCharacter(request):
    name=request.POST['name']
    character=Character(name=name, user_id=request.user.id)
    character.save()
    print(1)
    return redirect('/')