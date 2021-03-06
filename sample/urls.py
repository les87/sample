from django.conf.urls import patterns, include, url
from django.contrib import admin
from proto.forms import ExRegistrationForm
from registration.backends.default.views import RegistrationView
from proto import views

urlpatterns = patterns('', 
		(r'^calls/', include('proto.urls')),
		(r'^calls2/', include('proto.urls')),
		(r'^calls3/', include('proto.urls')),
		(r'^calls4/', include('proto.urls')),
	url(r'^admin/', include(admin.site.urls)),
	(r'^tinymce/', include('tinymce.urls')),
	
	    # ...

	url(r'accounts/register/$', 
        RegistrationView.as_view(form_class = ExRegistrationForm), 
        name = 'registration_register'),
	
	(r'^accounts/', include('registration.backends.default.urls')),
	url(r'^accounts/loggedin/', 'sample.views.loggedin'),
	url(r'^create_call/', 'proto.views.create_call'),
	url(r'^monitor/', 'proto.views.monitor'),
	url(r'^monitor2/', 'proto.views.monitor2'),
	url(r'^feedback/', 'proto.views.feedback'),
	url(r'^call/(?P<pk>[0-9]+)/update/$', views.call_update, name='call_update'),
	url(r'^call2/(?P<pk>[0-9]+)/update2/$', views.call_update2, name='call_update2'),
	
	url(r'^$', 'sample.views.index')

	
)
