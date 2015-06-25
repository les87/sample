from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
	email = forms.EmailField(required=True, widget=forms.TextInput
	(attrs={'placeholder': 'E-mail address'}))
	first_name = forms.CharField(required=True)
	last_name = forms.CharField(required=True)
	
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email','username', 'password1', 'password2')
	
	#clean email field 
	
	def clean_email(self):
		email = self.cleaned_data['email']
		try:
			User._default_manager.get(email=email)
		except User.DoesNotExist:
			return email
		raise forms.ValidationError('duplicate email')
	
	#modify save
	
	def save(self, commit=True):
		user = super(RegistrationForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.is_active = False # Will only be active link is clicked
			user.save()
		return user 
		