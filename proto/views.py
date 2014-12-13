from django.shortcuts import render_to_response, render, redirect
from proto.models import Call, Feedback
from proto.forms import CallForm, FeedbackForm
from django.template import RequestContext

def calls(request):
	if not request.user.is_authenticated():
		return redirect('/accounts/loggedin')
	else:
		return render_to_response('calls.html',
		{'calls': Call.objects.all().filter(resolved=False)})
							
def call(request, call_id=1):
	if not request.user.is_authenticated():
		return redirect('/accounts/loggedin')
	else:
		return render_to_response('call.html',
		{'call' : Call.objects.get(id=call_id)})
		if request.method == 'POST':
			form = EngineerCallForm(request.POST)
		if form.is_valid():
			call = form.save(commit=False)
			call.engineer = request.user
			call.save()
			return render('calls.html',
			{'calls': Call.objects.all().filter(resolved=False)})
		else:			
			form = EngineerCallForm()

			return render_to_response('calls.html',
			{'calls': Call.objects.all().filter(resolved=False)})

			
def create_call(request):
	if request.method == 'POST':
		form = CallForm(request.POST)
		if form.is_valid():
			call = form.save(commit=False)
			call.logged_by = request.user
			call.save()
			return redirect('/accounts/loggedin', pk=call.pk)
        else:
			form = CallForm()

			return render(request, 'create_call.html', {'form': form})
			
			
def monitor(request):
	if not request.user.is_authenticated():
		return redirect('/accounts/loggedin')
	else:
		return render_to_response('monitor.html',
		{'calls': Call.objects.all().filter(logged_by = request.user, resolved=False)})
	
	
def feedback(request):
	if request.method == 'POST':
		form = FeedbackForm(request.POST)
		if form.is_valid():
			feedback = form.save(commit=True)
			feedback.save()
			return redirect('/accounts/loggedin')
	else:
		form = FeedbackForm()
		form.fields['call'].queryset = Call.objects.filter(
		logged_by = request.user, resolved=True, feedback__description__isnull=True 
		).exclude(
		description='')

	return render(request, 'feedback.html', {'form': form})
	