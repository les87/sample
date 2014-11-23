from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.core.context_processors import csrf

def index(request):
	return render_to_response('index.html')

def login(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('login.html', c)

def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)
	
	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/accounts/loggedin')
	else:
		return HttpResponseRedirect('/accounts/invalid')
		
def loggedin(request):
	return render_to_response('loggedin.html',
							{'full_name': request.user.username})

def invalid_login(request):
	return render_to_response('invalid_login.html')
	
def logout(request):
	auth.logout(request)
	return render_to_response('logout.html')
	
def register(request):
	return render_to_response('register.html')
							