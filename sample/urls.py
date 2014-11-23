from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('', 
		(r'^printers/', include('proto.urls')),
	url(r'^admin/', include(admin.site.urls)),
)