# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Product, Category

class ProductAdmin(admin.ModelAdmin):
    pass

    search_fields = ['name', 'id']
    list_display = ('name', 'create_at', 'image','category')

admin.site.register(Product,  ProductAdmin)

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name_vi','name_en', 'id']
    list_display = ('name_vi', 'create_at')
    pass
admin.site.register(Category, CategoryAdmin)
