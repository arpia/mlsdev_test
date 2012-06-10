# -*- coding:utf-8 -*-

from forms import *
from models import user_profile

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

@login_required
def user_account (request):
    try:
        profile = user_profile.objects.get(username=request.user.username)
    except (user_profile.DoesNotExist):
        profile = request.user

    return render(request, 'profile.html', {
        'profile':profile,
        'user':request.user
        })

def user_login (request):
    if request.user.is_authenticated():
        return redirect('account_index')
    
    form = login_form(request.POST or None)
    if form.is_valid():
        login(request, form.get_user())
        return redirect(request.GET.get('next', '/'))

    return render(request, 'login.html',{
        'form':form
        })

def user_logout (request):
    if request.user.is_authenticated():
        logout(request)

    return redirect('/')

def user_registration (request):
    if request.user.is_authenticated():
        return redirect('account_index')

    form = registration_form(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        user_login(request)

        return redirect('/')

    return render(request, 'join.html',{
        'form':form
        })
