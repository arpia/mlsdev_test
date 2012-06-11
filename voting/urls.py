from django.conf.urls import patterns, include, url

from views import *

urlpatterns = patterns('',
	url(r'^question/(?P<number>\d+)/up/', vote_question_up),
	url(r'^question/(?P<number>\d+)/down/', vote_question_down),

	url(r'^answer/(?P<number>\d+)/up/', vote_answer_up),
	url(r'^answer/(?P<number>\d+)/down/', vote_answer_down),
	)