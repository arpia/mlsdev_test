# -*- coding:utf-8 -*-
#необходимо оптимизировать - слишком много повторяющегося кода

from models import *
from forum.models import question
from accounts.models import user_profile

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def vote_question_up (request, number):
	try:
		voted = question.objects.get(id=number)
	except question.DoesNotExist:
		return HttpResponse(0)
	voter = user_profile.objects.get(username=request.user.username)
	try:
		vote = question_voting.objects.get(voted=voted, voter=voter)
	except question_voting.DoesNotExist:
		vote = question_voting(voted=voted, voter=voter)

	vote.voteup()

	return HttpResponse(question.objects.get(id=number).rating)

@login_required
def vote_question_down (request, number):
	try:
		voted = question.objects.get(id=number)
	except question.DoesNotExist:
		return HttpResponse(0)
	voter = user_profile.objects.get(username=request.user.username)
	try:
		vote = question_voting.objects.get(voted=voted, voter=voter)
	except question_voting.DoesNotExist:
		vote = question_voting(voted=voted, voter=voter)

	vote.votedown()

	return HttpResponse(question.objects.get(id=number).rating)

@login_required
def vote_answer_up (request, number):
	try:
		voted = answer.objects.get(id=number)
	except answer.DoesNotExist:
		return HttpResponse(0)
	voter = user_profile.objects.get(username=request.user.username)
	try:
		vote = answer_voting.objects.get(voted=voted, voter=voter)
	except answer_voting.DoesNotExist:
		vote = answer_voting(voted=voted, voter=voter)

	vote.voteup()

	return HttpResponse(answer.objects.get(id=number).rating)

@login_required
def vote_answer_down (request, number):
	try:
		voted = answer.objects.get(id=number)
	except answer.DoesNotExist:
		return HttpResponse(0)
	voter = user_profile.objects.get(username=request.user.username)
	try:
		vote = answer_voting.objects.get(voted=voted, voter=voter)
	except answer_voting.DoesNotExist:
		vote = answer_voting(voted=voted, voter=voter)

	vote.votedown()

	return HttpResponse(answer.objects.get(id=number).rating)