# -*- coding:utf-8 -*-

from forms import *
from models import user_profile

from django.shortcuts import render_to_response, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

@login_required
def user_account (request):
    try:
        profile = user_profile.objects.get(username=request.user.username)
    except (user_profile.DoesNotExist):
        profile = request.user

    return render_to_response('profile.html', {
        'profile':profile,
        'user':request.user
        })

@csrf_protect
def user_login (request):
    if request.user.is_authenticated():
        return redirect('account_index')
    
    form = login_form(request.POST or None)
    if form.is_valid():
        login(request, form.get_user())
        return redirect(request.GET.get('next', '/'))

    return render_to_response('login.html',{
        'form':form
        })

def user_logout (request):
    if request.user.is_authenticated():
        logout(request)

    return redirect('/')

@csrf_protect
def user_registration (request):
    if request.user.is_authenticated():
        return redirect('account_index')

    form = registration_form(request.POST or None)
    if form.is_valid():
        form.save()
        user_login(request)

        return redirect('/')

    return render_to_response('join.html',{
        'form':form
        })
