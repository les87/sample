from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('', 
		(r'^calls/', include('proto.urls')),
	url(r'^admin/', include(admin.site.urls)),
	
	
	#User auth urls
	url(r'^accounts/login/$', 'sample.views.login'),
	url(r'^accounts/auth/$', 'sample.views.auth_view'),
	url(r'^accounts/logout/$', 'sample.views.logout'),
	url(r'^accounts/logout/accounts/login$', 'sample.views.login'),
	url(r'^accounts/logout/accounts/register$', 'sample.views.register'),
	url(r'^accounts/loggedin/$', 'sample.views.loggedin'),
	url(r'^accounts/invalid/$', 'sample.views.invalid_login'),
	url(r'^accounts/register/$', 'sample.views.register'),
	url(r'^$', 'sample.views.index')
)
