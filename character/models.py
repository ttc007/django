# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from products.models import Product
from django.contrib.auth.models import User


# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True, null=True)
    level = models.IntegerField(default=1)
    hp = models.IntegerField(default=1000)
    armor = models.IntegerField(default=32)
    acttack = models.IntegerField(default=90)
    gold = models.IntegerField(default=10000)
    image = models.FileField(upload_to='images/', default='default.jpg')

    weapon = models.IntegerField(null=True)
    armour = models.IntegerField(null=True)
    foot = models.IntegerField(null=True)
    def __str__(self):
        return '%s' % (self.name)

    def weaponOp(self):
        return Product.objects.get(id=self.weapon)
    def footOp(self):
        return Product.objects.get(id=self.foot)
    def armourOp(self):
        return Product.objects.get(id=self.armour)
    def vaults(self):
        return Vault.objects.filter(character_id=self.id)

class Vault(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE, null=True,
                                  blank=True)
    item = models.IntegerField(null=True)
    def product(self):
        return Product.objects.get(id=self.item)