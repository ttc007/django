# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Product, Category

class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        ("Category", {'fields': ['category']}),
        ('Date information', {'fields': ['create_at']})
    ]
    search_fields = ['name', 'id']
    list_display = ('name', 'create_at', 'image','category_id', 'category_name')
    def category_name(self, obj):
        return obj.category.name

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "category":
            kwargs["queryset"] = Category.objects.all()
        return super(ProductAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        ('Date information', {'fields': ['create_at']}),
    ]
    list_display = ('id', 'name', 'create_at')

admin.site.register(Product,  ProductAdmin)
admin.site.register(Category, CategoryAdmin)
