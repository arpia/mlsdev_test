# -*- coding:utf-8 -*-

from models import *

from django.shortcuts import render_to_response, redirect
from django.utils.translation import ugettext_lazy as _

def forum (request, number=0):
	questions_per_page = 10

	number = int(number)
	first_question = number*questions_per_page
	last_question = (number + 1)*questions_per_page

	questions = question.objects.all()[first_question:last_question]

	return render_to_response('forum.html',
		'questions':questions
		)

def one_question (request, number):
	return redirect('http://google.com')