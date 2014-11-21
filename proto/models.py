from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator 

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