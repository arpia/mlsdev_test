# -*- coding:utf-8 -*-

from models import *
from forms import *

from django.shortcuts import render, redirect
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

	form = answer_form(initial={'question':number})

	return render(request, 'question.html', {
		'question':cur_question,
		'answers':answers,
		'form':form
		})

def add_answer (request):
	form = answer_form(request.POST or None)
	if form.is_valid():
		form.save()
		question.objects.get(id=request.POST.get('question')).inc_answers()

	next = '/'
	if request.POST.get('question'):
		next = '/question/' + request.POST.get('question')

	return redirect(next)