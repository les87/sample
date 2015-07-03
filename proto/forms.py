from registration.forms import RegistrationForm
from django import forms
from django.contrib.auth.models import User, Group
from proto.models import Call, Printer, Feedback, Knowledge
from django.forms import ModelForm, ModelChoiceField, Select
 
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
    engineer = ModelChoiceField(queryset=User.objects.all().filter(is_staff=True),
                              widget=Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Call
        fields = ('engineer', 'engineer_comment', 'status')
        widgets = {
 		  'engineer_comment': forms.Textarea(attrs={'rows':5, 'cols':40})}

# class UpdateCallForm(forms.ModelForm):

#     engineer = forms.ModelChoiceField(
#         queryset=Call.objects.all(),
#         label='Engineer',
#         required=False,
#         widget=forms.Select(attrs={'class': 'form-control'})
#     )

# 	#engineer = Call.objects.all(),
# 	class Meta:
# 		model = Call
# 		fields = ('engineer_comment', 'engineer', 'status')
# 		#widgets = {
# 		#  'engineer_comment': forms.Textarea(attrs={'rows':5, 'cols':40}),
#   		#  'engineer': forms.Select(attrs={'class': 'select'}),

#         #}	


		
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

