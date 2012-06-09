# -*- coding:utf-8 -*-

from models import *

from django.shortcuts import render_to_response, redirect
from django.utils.translation import ugettext_lazy as _

def forum (request, number=1):
	questions_per_page = 10

	number = int(number)
	first_question = (number - 1)*questions_per_page
	last_question = number*questions_per_page

	questions = question.objects.all()[first_question:last_question]

	question_count = question.objects.all().count()
	current_page = number
	total_pages = question_count / questions_per_page
	if question_count % questions_per_page > 0:
		total_pages += 1

	return render_to_response('forum.html', {
		'questions':questions,
		'current_page':current_page,
		'total_pages':total_pages
		})

def one_question (request, number=1):
	cur_question = question.objects.get(id=number)
	cur_question.inc_view()

	return render_to_response('question.html', {
		'question':cur_question
		})