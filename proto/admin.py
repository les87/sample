from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from proto.models import ExUserProfile
from proto.models import Call, Printer, Feedback, Knowledge
from django import forms
from django.db import models


admin.site.unregister(User)

class UserProfileInline(admin.StackedInline):
    model = ExUserProfile

class UserProfileAdmin(UserAdmin):
    inlines = [ UserProfileInline, ]

class CKAdmin(admin.ModelAdmin):
    formfield_overrides = { models.TextField: {'widget': forms.Textarea(attrs={'class':'ckeditor'})}, }

    class Media:

    	css = {
    		"all": ('css/formatfix.css',)
    	}
        js = ('ckeditor/ckeditor/ckeditor.js',)


admin.site.register(User, UserProfileAdmin)

admin.site.register(Call)
admin.site.register(Printer)
admin.site.register(Feedback)
admin.site.register(Knowledge, CKAdmin)