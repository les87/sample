from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator 
from django.contrib.auth.models import User
from registration.signals import user_registered

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
	description = models.TextField()
	engineer_comment = models.TextField(blank=True)
	logged_by = models.CharField(max_length=30, blank=True)
	Resolved = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	
		
	def __unicode__(self):
		return "Call # - "'%s %s' % (self.id, self.printer)
	

class Feedback(models.Model):
	call = models.ForeignKey(Call)
	rating = models.IntegerField (validators=[MinValueValidator(0),MaxValueValidator(10)])
	description = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	
	def __unicode__(self):
		return "Feedback for - "'%s' % (self.call)
		
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