# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-07 19:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Item', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='PID',
        ),
    ]
