# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)
    create_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return '%s' % (self.name)

class Product(models.Model):
    name = models.CharField(max_length=200)
    create_at = models.DateTimeField(auto_now_add=True, null= True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts_type_rel', null=True,
                                  blank=True)
    image = models.FileField(upload_to='images/', default='default.jpg')

    def __str__(self):
        return '%s' % (self.name)



