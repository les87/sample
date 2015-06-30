from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator 
from django.contrib.auth.models import User
from registration.signals import user_registered
from django.forms import ModelForm

class Printer(models.Model): 
	serial_number = models.CharField(max_length=200, unique=True) 
	asset_tag = models.CharField(max_length=200, unique=True)
	model = models.CharField(max_length=200)
	name = models.CharField(max_length=200)
	location = models.CharField(max_length=200)
	ip_address = models.GenericIPAddressField(unpack_ipv4=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	
	def __unicode__(self):
		return u'%s %s' % (self.name, self.serial_number)
	

class Call(models.Model): 
	printer = models.ForeignKey(Printer)

	category_choices = (
		('PS', 'Printer Setup'),
		('PJ', 'Printer Jam'),
		('NT', 'No Toner'),
		('PP', 'Power Problem'),
		('EC', 'Error Code'),
		('OT', 'Other'),
	)
	category = models.CharField(max_length=2, choices=category_choices, default="<Category Not Selected>") 
	
	description = models.TextField()
	engineer = models.CharField(max_length=30, default="No Engineer Assigned", blank=True)
	engineer_comment = models.TextField(blank=True)
	logged_by = models.CharField(max_length=30, blank=True)
	resolved = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	
		
	def __unicode__(self):
		return "Call # - "'%s %s' % (self.id, self.printer)
	

class Feedback(models.Model):
	call = models.ForeignKey(Call)
	rating_choices = (
		(1, '1 - Poor'),
		(2, '2'),
		(3, '3'),
		(4, '4'),
		(5, '5 - Average'),
		(6, '6'),
		(7, '7'),
		(8, '8'),
		(9, '9'),
		(10, '10 - Excellent'),
	)

	rating = models.IntegerField (choices=rating_choices, default=10)
	description = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	
	def __unicode__(self):
		return "Feedback for - "'%s' % (self.call)
		

class Knowledge(models.Model):
	title = models.CharField(max_length=200, unique=True) 
	problem = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return "Knowledge Article - "'%s %s' % (self.id, self.title)

class ExUserProfile(models.Model):
	user = models.ForeignKey(User, unique=True)
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
 
	def __unicode__(self):
		return self.user
	
	def user_registered_callback(sender, user, request, **kwargs):
		profile = ExUserProfile(user = user)
		user.first_name = request.POST['first_name']
		user.last_name = request.POST['last_name']
		user.save()
		profile.save()
	
	def __unicode__(self):
		return '%s' % (self.user)
		
	user_registered.connect(user_registered_callback)




