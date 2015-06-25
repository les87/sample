from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^all/$', 'proto.views.calls'),
	url(r'^get/(?P<call_id>\d+)/$', 'proto.views.call'),
	
)