# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-12 09:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20170612_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category_id',
            field=models.ForeignKey(choices=[(1, 'Food'), (2, 'Electronic'), (4, 'Motorbike')], on_delete=django.db.models.deletion.CASCADE, to='products.Category'),
        ),
    ]
