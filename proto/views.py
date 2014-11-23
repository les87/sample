from django.shortcuts import render_to_response
from proto.models import Printer

def printers(request):
	return render_to_response('printers.html',
							{'printers': Printer.objects.all()})
							
def printer(request, printer_id=1):
	return render_to_response('printer.html',
							{'printer' : Printer.objects.get(id=printer_id)})
					
