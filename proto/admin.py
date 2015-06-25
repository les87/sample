from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from proto.models import ExUserProfile
from proto.models import Call, Printer, Feedback, Knowledge


class UserProfileInline(admin.StackedInline):
    model = ExUserProfile

class UserProfileAdmin(UserAdmin):
    inlines = [ UserProfileInline, ]

admin.site.unregister(User)
admin.site.register(User, UserProfileAdmin)

admin.site.register(Call)
admin.site.register(Printer)
admin.site.register(Feedback)
admin.site.register(Knowledge)