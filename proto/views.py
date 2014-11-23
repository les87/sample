from django.shortcuts import render_to_response
from proto.models import Call

def calls(request):
	return render_to_response('calls.html',
							{'calls': Call.objects.all()})
							
def call(request, call_id=1):
	return render_to_response('call.html',
							{'call' : Call.objects.get(id=call_id)})
					
