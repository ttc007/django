# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import auth
from django.contrib.auth.models import User
from login.forms import *
def login_view(request):
    return render(request, 'login/login.html')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username, password=password)
    if user is not None:
        # if user.is_active:
        auth.login(request, user)
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
    if request.POST['password'] == request.POST['password_again'] :
        user = User(username=request.POST['username'],
                email=request.POST['email'],
                password=request.POST['password'])
        user.set_password(request.POST['password'])
        user.save()
        auth.login(request, user)
        return redirect('/')
    error = "Password again not match"
    return render(request, 'login/register.html',{'error':error})
