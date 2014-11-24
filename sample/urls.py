from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('', 
		(r'^calls/', include('proto.urls')),
	url(r'^admin/', include(admin.site.urls)),
	(r'^accounts/', include('registration.backends.default.urls')),
	url(r'^accounts/loggedin/', 'sample.views.loggedin'),
	
	url(r'^$', 'sample.views.index')
	
)
