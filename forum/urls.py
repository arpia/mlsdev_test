from django.conf.urls import patterns, include, url

from forum.views import *

urlpatterns = patterns('',
	url(r'^$', forum, name='forum'),
	url(r'^(?P<number>\d{1,3})/$', forum),

	url(r'^question/$', one_question),
	url(r'^question/(?P<number>\d{1,3})/', one_question),

	url(r'^ask/$', manage_question),
    url(r'^edit/(?P<number>\d{1,3})$', manage_question),
    # url(r'^delete/(?P<number>\d{1,2})$', delete_question),

	url(r'^answer/$', add_answer),
	)