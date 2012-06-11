# -*- coding:utf-8 -*-

from models import *
from forms import *
from accounts.models import user_profile

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext_lazy as _

def forum (request, number=1):
	questions_per_page = 10

	number = int(number)
	first_question = (number - 1)*questions_per_page
	last_question = number*questions_per_page

	questions = question.objects.order_by('-date')[first_question:last_question]

	question_count = question.objects.all().count()
	current_page = number
	total_pages = question_count / questions_per_page
	if question_count % questions_per_page > 0:
		total_pages += 1

	return render(request, 'forum.html', {
		'questions':questions,
		'current_page':current_page,
		'total_pages':total_pages
		})

def one_question (request, number=1):
	cur_question = question.objects.get(id=number)
	cur_question.inc_view()

	answers = cur_question.answer_set.order_by('-rating')

	if request.user.is_authenticated():
		form = answer_form(initial={
			'question':number,
			'sender':user_profile.objects.get(username=request.user.username)
			})
	else:
		form = None

	return render(request, 'question.html', {
		'question':cur_question,
		'answers':answers,
		'form':form
		})

@login_required
def add_answer (request):
	form = answer_form(request.POST or None)
	if form.is_valid():
		new_answer = form.save()
		question.objects.get(id=request.POST.get('question')).inc_answers()

		return render(request, 'answer.html',{
			'answer':new_answer
			})

@login_required
def manage_question (request, number=None):
    if number:
        form_type = _(u'Edit')
        number = int(number)

        try:
            question.objects.get(id=number)
        except question.DoesNotExist:
            return redirect('forum')

        if question.objects.get(id=number).sender.username != request.user.username:
        	return redirect('forum')

        form = question_form(request.POST or None, instance=question.objects.get(id=number))
        if form.is_valid():
        	form.save()
        	return redirect('forum') #change to redirect for newly edited question
    else:
        form_type = _(u'Ask')
        form = question_form(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('forum') #change to redirect for newly added question

        form = question_form(initial={'sender':user_profile.objects.get(username=request.user.username)})
    
    return render(request, 'manage_question.html', {
        'form':form,
        'type':form_type
        })

@login_required
def delete_question (request, number=None):
	number = int(number)
	try:
		question.objects.get(id=number)
	except question.DoesNotExist:
		return redirect('forum')

	if question.objects.get(id=number).sender.username != request.user.username:
		return redirect('forum')
	
	question.objects.get(id=number).delete()

	return redirect('forum')