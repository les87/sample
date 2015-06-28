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
    exclude = ('first_name', 'last_name')

    class Media:
    
        css = { "all" : ("css/useradmin.css",) }

class UserProfileAdmin(UserAdmin):
    inlines = [ UserProfileInline, ]


class TinyAdmin(admin.ModelAdmin):

    class Media:

    	css = {
    		"all": ('css/formatfix.css',)
    	}
        js = ('js/tinymce/tinymce.min.js','js/tinymce/tinyinit.js')


class ReadOnlyAdmin(admin.ModelAdmin):
    actions = None
    readonly_fields = []

    def get_readonly_fields(self, request, obj=None):
        return list(self.readonly_fields) + \
               [field.name for field in obj._meta.fields]
        
       

    def has_add_permission(self, request, obj=None):
        return False

        def has_delete_permission(self, request, obj=None):
            return False

    class Media:
        css = {'all':('/static/css/admin.css',)}



admin.site.register(User, UserProfileAdmin)

admin.site.register(Call, ReadOnlyAdmin)
admin.site.register(Printer)
admin.site.register(Feedback, ReadOnlyAdmin)
admin.site.register(Knowledge, TinyAdmin)