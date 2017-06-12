# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)
    create_at = models.DateTimeField('date published')


class Product(models.Model):
    CATEGORYS = []
    for category in Category.objects.all():
        CATEGORYS.append((category.id, category.name))

    name = models.CharField(max_length=200)
    create_at = models.DateTimeField('date published')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1, related_name="products",
        related_query_name="product")
    image = models.FileField(upload_to='images/', default='default.jpg')



