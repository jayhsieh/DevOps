# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-17 10:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0003_auto_20170817_1811'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='script',
            name='author',
        ),
    ]
