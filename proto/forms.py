from registration.forms import RegistrationForm
from django import forms
from proto.models import Call, Printer, Feedback, Knowledge

 
class ExRegistrationForm(RegistrationForm):
	first_name = forms.CharField(max_length=30)
	last_name = forms.CharField(max_length=30)
	
class CallForm(forms.ModelForm):

	class Meta:
		model = Call
		fields = ('printer', 'category', 'description')
		widgets = {
          'description': forms.Textarea(attrs={'rows':5, 'cols':40}),
        }	

class UpdateCallForm(forms.ModelForm):

	class Meta:
		model = Call
		fields = ('engineer_comment', 'status')
		widgets = {
		  'engineer_comment': forms.Textarea(attrs={'rows':5, 'cols':40}),
        }	
		
class FeedbackForm(forms.ModelForm):
	
	class Meta:
		model = Feedback
		fields = ('call', 'rating', 'description')
		widgets = {
          'description': forms.Textarea(attrs={'rows':5, 'cols':40}),
        }
    


class KnowledgeForm(forms.ModelForm):
	
	class Meta:
		model = Knowledge
		fields = ('title', 'problem')
		widgets = {
		  'problem': forms.Textarea(attrs={'rows':5, 'cols':40}),
        }    

class UpdateKnowledgeForm(forms.ModelForm):

	class Meta:
		model = Knowledge
		fields = ('title', 'problem')
		widgets = {
		  'problem': forms.Textarea(attrs={'rows':5, 'cols':40}),
        }

