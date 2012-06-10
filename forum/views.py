# -*- coding:utf-8 -*-

from models import *
from forms import *

from django.shortcuts import render, redirect
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

	form = answer_form(initial={'question':number})

	return render(request, 'question.html', {
		'question':cur_question,
		'answers':answers,
		'form':form
		})

@login_required
def add_answer (request):
	form = answer_form(request.POST or None)
	if form.is_valid():
		form.save()
		question.objects.get(id=request.POST.get('question')).inc_answers()

	next = '/'
	if request.POST.get('question'):
		next = '/question/' + request.POST.get('question')

	return redirect(next)

@login_required
def manage_question (request, number=None):
    if number:
        form_type = _(u'Edit')
        number = int(number)

        try:
            question.objects.get(id=number)
        except (question.DoesNotExist):
            return redirect('forum')

        if request.method == 'POST':
            form = question_form(request.POST)

            if form.is_valid():
                form.save()
                return redirect('forum') #change to redirect for newly added question
        else:
            form = lesson_form(instance=text_lesson.objects.get(id=number))
    else:
        form_type = _(u'Add')
        form = lesson_form(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('lessons_index')        
    
    return render_to_response('manage_lesson.html', {
        'form':form,
        'type':form_type,
        'user':request.user,
        'csrfmiddlewaretoken':csrf_token(RequestContext(request))
        })