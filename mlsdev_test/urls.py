import os

from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mlsdev_test.views.home', name='home'),
    # url(r'^mlsdev_test/', include('mlsdev_test.foo.urls')),

    url(r'^accounts/', include('accounts.urls')),
    url(r'^', include('forum.urls')),

	url(r'^admin/', include(admin.site.urls)),
	url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
    	'document_root': os.getcwd() + '/media/'
    	}),
	
	url(r'^captcha/', include('captcha.urls')),
)
