from django.shortcuts import render_to_response, render, redirect, get_object_or_404
from proto.models import Call, Feedback, Knowledge
from proto.forms import CallForm, FeedbackForm, UpdateCallForm, KnowledgeForm, UpdateCallForm2
from django.template import RequestContext
from django.core.mail import EmailMessage

def calls(request):
	if not request.user.is_authenticated():
		return redirect('/accounts/loggedin')
	else:
		return render_to_response('calls.html',
		{'calls': Call.objects.all().filter(status='Unassigned')})

def calls2(request):
	if not request.user.is_authenticated():
		return redirect('/accounts/loggedin')
	else:
		return render_to_response('calls2.html',
		{'calls': Call.objects.all().filter(status='Assigned')})

def calls3(request):
	if not request.user.is_authenticated():
		return redirect('/accounts/loggedin')
	else:
		return render_to_response('calls3.html',
		{'calls': Call.objects.all().filter(status='Delayed')})

def calls4(request):
	if not request.user.is_authenticated():
		return redirect('/accounts/loggedin')
	else:
		return render_to_response('calls4.html',
		{'calls': Call.objects.all().exclude(status='Resolved')})		
							
def call(request, call_id=1):
	if not request.user.is_authenticated():
		return redirect('/accounts/loggedin')
	else:
		return render_to_response('call.html',
		{'call' : Call.objects.get(id=call_id)})

def call2(request, call_id=1):
	if not request.user.is_authenticated():
		return redirect('/accounts/loggedin')
	else:
		return render_to_response('call2.html',
		{'call' : Call.objects.get(id=call_id)})		
				

def call_update(request, pk):
    call = get_object_or_404(Call, pk=pk)
    if request.method == "POST":
        form = UpdateCallForm(request.POST, instance=call)
        if form.is_valid():
            call = form.save(commit=True)
            call.engineer = request.user.first_name
             
            call.save()
            
            subject = 'There has been an update on your Incident'
            body = 'Hello!' + '\n' + '\n' + call.engineer_comment + '\n' + '\n'
            body2 = 'STATUS:' + '  ' + call.status + '\n' + '\n'
            body3 = 'Regards' + '\n' + '\n' + call.engineer
            	
            
            email = EmailMessage(subject, body + body2 + body3, 'Print Support Updates',
            to=[call.logged_by])
            email.send()

            return redirect('/accounts/loggedin')
    else:
        form = UpdateCallForm(instance=call)
    return render(request, 'call_update.html', {'form': form})


def call_update2(request, pk):
    call = get_object_or_404(Call, pk=pk)
    if request.method == "POST":
        form = UpdateCallForm2(request.POST, instance=call)
        if form.is_valid():
            call = form.save(commit=True)
                         
            call.save()
            
            subject = 'This call has now been assigned to you'
            body = 'Hello!' + '\n' + '\n' + call.description + '\n' + '\n'
            body2 = 'Engineer Comments: ' + call.engineer_comment + '\n' + '\n'
            body3 = 'STATUS:' + '  ' + call.status           	
            
            email = EmailMessage(subject, body + body2 + body3, 'Print Support Updates',
            to=[call.engineer])
            email.send()

            return redirect('/accounts/loggedin')
    else:
        form = UpdateCallForm2(instance=call)
    return render(request, 'call_update2.html', {'form': form})    
			
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

def create_knowledge(request):
	if request.method == 'POST':
		form = KnowledgeForm(request.POST)
		if form.is_valid():
			knowledge = form.save(commit=False)
			knowledge.save()
			return redirect('/accounts/loggedin', pk=call.pk)
        else:
			form = KnowledgeForm()

			return render(request, 'create_knowledge.html', {'form': form})

def knowledge_update(request, pk):
    knowledge = get_object_or_404(Call, pk=pk)
    if request.method == "POST":
        form = UpdateKnowledgeForm(request.POST, instance=call)
        if form.is_valid():
            knowledge = form.save(commit=True)
            return redirect('/accounts/loggedin')
    else:
        form = UpdateCallForm(instance=call)
    return render(request, 'knowledge_update.html', {'form': form})	
  		
			
def monitor(request):
	if not request.user.is_authenticated():
		return redirect('/accounts/loggedin')
	else:
		return render_to_response('monitor.html',
		{'calls': Call.objects.all().filter(logged_by = request.user)})
	
	
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
		logged_by = request.user, status='Resolved', feedback__description__isnull=True 
		).exclude(
		description='')

	return render(request, 'feedback.html', {'form': form})


def rating(request):
    f = Call.objects.filter(
    engineer = request.user, status='Resolved')
    rating_average = f.rating_set.aggregate(Avg('rating')).values()[0]

	