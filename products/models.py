# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Industry(models.Model):
    name = models.CharField(max_length=200)
    create_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return '%s' % (self.name_en)

    def categorys(self):
        return Category.objects.fillter(industry_id=self.id)

class Category(models.Model):
    name = models.CharField(max_length=200)
    industry = models.ForeignKey(Industry,on_delete=models.CASCADE, null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return '%s' % (self.name_en)

    def products(self):
        return Product.objects.fillter(industry_id=self.id)

class Product(models.Model):
    name = models.CharField(max_length=200)
    create_at = models.DateTimeField(auto_now_add=True, null= True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts_type_rel', null=True,
                                  blank=True)
    image = models.FileField(upload_to='images/', default='default.jpg')
    HP = models.IntegerField(default=1000)
    Armor = models.IntegerField(default=32)
    Acttack = models.IntegerField(default=90)
    def __str__(self):
        return '%s' % (self.name)



