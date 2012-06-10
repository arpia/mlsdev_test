from django.conf.urls.defaults import *

from views import *

urlpatterns = patterns('',
    url(r'^$', user_account, name='account_index'),
    url(r'^login', user_login),
    url(r'^logout$', user_logout),
    url(r'^join$', user_registration),
)
