# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Product, Category

class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        ('Date information', {'fields': ['create_at']}),
    ]
    list_display = ('name', 'create_at', 'image')

class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        ('Date information', {'fields': ['create_at']}),
    ]
    list_display = ('name', 'create_at')
admin.site.register(Product,  ProductAdmin)
admin.site.register(Category, CategoryAdmin)
