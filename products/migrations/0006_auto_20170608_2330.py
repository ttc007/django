# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-08 16:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20170608_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='create_at',
            field=models.DateTimeField(verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='product',
            name='create_at',
            field=models.DateTimeField(verbose_name='date published'),
        ),
    ]
