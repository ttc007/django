# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-07 14:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='create_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='create_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]