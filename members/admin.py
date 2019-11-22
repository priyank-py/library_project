from django.contrib import admin
from .models import Member
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


class MemberInline(admin.StackedInline):
    model = Member
    extra = 1
    max_num = 1
    min_num = 1

class MemberAdmin(UserAdmin):
    inlines = (MemberInline,)


    
admin.site.unregister(User)
admin.site.register(User, MemberAdmin)
