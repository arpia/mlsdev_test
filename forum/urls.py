from django.conf.urls import patterns, include, url

from forum.views import *

urlpatterns = patterns('',
	url(r'^$', forum),
	url(r'^(?P<number>\d{1,3})/$', forum),
	url(r'^question/$', one_question),
	url(r'^question/(?P<number>\d{1,3})/', one_question),
	)