from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.template import RequestContext
from django.contrib.auth.models import Group

def index(request):
	return render_to_response('index.html')

def loggedin(request):
	user = request.user
	if user.is_authenticated():
		if user.groups.filter(name='Engineers'):
			return render_to_response('loggedin2.html', context_instance=RequestContext(request))
		else:
			return render_to_response('loggedin.html', context_instance=RequestContext(request))
	else: 
		return render_to_response('index.html')