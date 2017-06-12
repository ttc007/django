# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    create_at = models.DateTimeField('date published')
    category_id = models.IntegerField(default=1)
    image = models.FileField(upload_to='images/', default='default.jpg')

class Category(models.Model):
    name = models.CharField(max_length=200)
    create_at = models.DateTimeField('date published')