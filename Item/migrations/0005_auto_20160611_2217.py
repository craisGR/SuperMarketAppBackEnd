# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-11 19:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Item', '0004_auto_20160611_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='COVERURL',
            field=models.URLField(null=True),
        ),
    ]
