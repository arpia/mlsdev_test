from django.conf.urls import patterns, include, url

from views import *

urlpatterns = patterns('',
	url(r'^$', forum, name='forum'),
	url(r'^(?P<number>\d+)/$', forum),
	url(r'^(?P<bytag>\w+)/$', forum),

	url(r'^question/$', one_question),
	url(r'^question/(?P<number>\d+)/$', one_question),

	url(r'^ask/$', manage_question),
    url(r'^edit/(?P<number>\d+)/$', manage_question),
    url(r'^delete/(?P<number>\d+)/$', delete_question),

	url(r'^answer/$', add_answer),

	url(r'^addtag/(?P<tag_title>\w+)/$', add_tag),
	)