# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Product, Category, Industry

class ProductAdmin(admin.ModelAdmin):
    pass
    # fields = ('name_en', 'name_vi', 'image', 'category')
    search_fields = ['name_en','name_vi', 'id']
    list_display = ('id', 'name', 'create_at', 'image', 'category')

admin.site.register(Product,  ProductAdmin)

class CategoryAdmin(admin.ModelAdmin):
    fields = ('name_en', 'name_vi', 'industry')
    search_fields = ['name_en','name_vi', 'id']
    list_display = ('name', 'industry','create_at')
    pass
admin.site.register(Category, CategoryAdmin)

class IndustryAdmin(admin.ModelAdmin):
    fields = ('name_en', 'name_vi')
    search_fields = ['name_en','name_vi', 'id']
    list_display = ('name', 'create_at')
    pass
admin.site.register(Industry, IndustryAdmin)

