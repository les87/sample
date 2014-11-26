from django.shortcuts import render_to_response, render, redirect
from proto.models import Call
from proto.forms import CallForm

def calls(request):
	return render_to_response('calls.html',
							{'calls': Call.objects.all()})
							
def call(request, call_id=1):
	return render_to_response('call.html',
							{'call' : Call.objects.get(id=call_id)})
					
def create_call(request):
	if request.method == "POST":
		form = CallForm(request.POST)
		if form.is_valid():
			call = form.save(commit=False)
			call.logged_by = request.user
			call.save()
			return redirect('/accounts/loggedin', pk=call.pk)
        else:
			form = CallForm()

			return render(request, 'create_call.html', {'form': form})