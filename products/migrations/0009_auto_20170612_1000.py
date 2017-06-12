# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-12 10:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20170612_0940'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='product',
            managers=[
                ('manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='category_id',
            field=models.OneToOneField(choices=[(1, 'Food'), (2, 'Electronic'), (4, 'Motorbike')], on_delete=django.db.models.deletion.CASCADE, to='products.Category', verbose_name='related category'),
        ),
    ]
