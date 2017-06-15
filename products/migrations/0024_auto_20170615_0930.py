# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-15 09:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0023_auto_20170615_0822'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Acttack',
            field=models.IntegerField(default=90),
        ),
        migrations.AddField(
            model_name='product',
            name='Armor',
            field=models.IntegerField(default=32),
        ),
        migrations.AddField(
            model_name='product',
            name='HP',
            field=models.IntegerField(default=1000),
        ),
    ]