from django.contrib import admin
from users.models import NewUser
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea, CharField
from django import forms
from django.db import models

class UserAdminConfig(UserAdmin):
    model = NewUser
    search_fields = ('email', 'user_name', 'first_name',)
    list_filter = ('email', 'user_name',)
    ordering = ('-start_date',)
    list_display = ('email', 'user_name', 'first_name', 'is_staff')

    fieldsets = (
        (None, {'fields': ('email', 'user_name', 'first_name', 'password')}),
        ('Permissions', {'fields': ('is_staff',)}),
        ('Personal', {'fields': ('mob_num',)}),
    )

    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 20, 'cols': 60})},
    }

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields':  ('email', 'user_name', 'first_name', 'password1', 'password2', 'is_staff')
        }),
    )

admin.site.register(NewUser, UserAdminConfig)