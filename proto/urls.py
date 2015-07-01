from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^all/$', 'proto.views.calls'),
	url(r'^get/(?P<call_id>\d+)/$', 'proto.views.call'),
	url(r'^all2/$', 'proto.views.calls2'),
	url(r'^get/(?P<call_id>\d+)/$', 'proto.views.call2'),
	url(r'^all3/$', 'proto.views.calls3'),
	url(r'^get/(?P<call_id>\d+)/$', 'proto.views.call3'),
	
)