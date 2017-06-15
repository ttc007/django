# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Character

# Register your models here.
class CharacterAdmin(admin.ModelAdmin):
    # fields = ('name', 'level')
    search_fields = ['name', 'id']
    list_display = ('name', 'level', 'create_at')
    pass
admin.site.register(Character, CharacterAdmin)
