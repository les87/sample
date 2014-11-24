from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth

def index(request):
	return render_to_response('index.html')

def loggedin(request):
	return render_to_response('loggedin.html')
